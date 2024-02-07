import time
import threading
import queue
from google.cloud import speech


def transcribe_streaming(streaming_config, audio_stream, result_queue):
    client = speech.SpeechClient()

    # 실시간 스트리밍 음성 인식 설정
    requests = (
        speech.StreamingRecognizeRequest(audio_content=chunk)
        for chunk in audio_stream
    )

    # 실시간 스트리밍 음성 인식 요청
    responses = client.streaming_recognize(streaming_config, requests)

    # 결과 처리
    for response in responses:
        for result in response.results:
            result_queue.put(result.alternatives[0].transcript)

def process_transcripts(result_queue):
    while True:
        transcript = result_queue.get()
        print("Transcript: {}".format(transcript))

# 오디오 스트림 처리 및 음성 인식 시작
def start_transcription():
    streaming_config = speech.StreamingRecognitionConfig(
        config=speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        ),
        interim_results=True,
    )

    audio_stream = generate_audio_stream()  # 오디오 스트림 생성 함수

    result_queue = queue.Queue()

    # 실시간 음성 인식을 위한 스레드 시작
    transcription_thread = threading.Thread(
        target=transcribe_streaming,
        args=(streaming_config, audio_stream, result_queue),
    )
    transcription_thread.start()

    # 인식 결과 처리를 위한 스레드 시작
    processing_thread = threading.Thread(
        target=process_transcripts,
        args=(result_queue,),
    )
    processing_thread.start()

    # 일정 시간 동안 실행
    time.sleep(30)

    # 음성 인식 종료
    audio_stream.close()
    transcription_thread.join()
    processing_thread.join()

# 음성 인식 시작
start_transcription()
