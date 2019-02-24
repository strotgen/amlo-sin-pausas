from pydub import AudioSegment
import webrtcvad
import argparse


def read_file(filename):
    """Reads an audiofile in several formats and converts it
    to the appropriate format for the webrtcvad library.
    """
    audio = AudioSegment.from_file(filename)
    converted = audio.set_channels(1).set_frame_rate(32000).set_sample_width(2)
    return audio, converted.raw_data, converted.frame_rate


def frame_generator(frame_duration_ms, audio, sample_rate):
    """Generates audio frames from PCM audio data.
    Takes the desired frame duration in milliseconds, the PCM data, and
    the sample rate.
    Yields Frames of the requested duration.
    """
    n = int(sample_rate * (frame_duration_ms / 1000.0) * 2)
    offset = 0
    timestamp = 0.0
    duration = (float(n) / sample_rate) / 2.0
    while offset + n < len(audio):
        yield Frame(audio[offset:offset + n], timestamp, duration)
        timestamp += duration
        offset += n


class Frame(object):
    """Represents a "frame" of audio data."""

    def __init__(self, bytes, timestamp, duration):
        self.bytes = bytes
        self.timestamp = timestamp
        self.duration = duration


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove the pauses from AMLO's speeches.")
    parser.add_argument('inputfile', metavar='INPUTAUDIO', help="Full path to AMLO's audio file")
    parser.add_argument('outputfile', metavar='OUTPUTFILE', help='Full path to output file')
    args = parser.parse_args()

    vad = webrtcvad.Vad()
    vad.set_mode(3)
    real, converted_audio, converted_sample_rate = read_file(args.inputfile)
    frames = list(frame_generator(20, converted_audio, converted_sample_rate))
    audio_no_silence = real[0:0]
    for frame in frames:
        is_speech = vad.is_speech(frame.bytes, converted_sample_rate)
        if is_speech:
            start = frame.timestamp * 1000
            end = start + (frame.duration * 1000)
            audio_no_silence += real[start:end]
    audio_no_silence.export(args.outputfile, format="mp3")
