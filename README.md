# gcp-speech-to-text

## Pre-Requisites

1. Python 3.* or higher (necessary for the GCP SDK and the the NLP Library used) is where I tested, but it should run on Python 2.7 onwards.
2. [Google Cloud SDK](https://cloud.google.com/sdk/) installed
3. Google Cloud [Speech-to-Text API](https://cloud.google.com/speech/) enabled and working with your GCP configuration - `gcloud init`
4. Besides core Python packages you need to `pip3 install -r requirements.txt`

----

## Step 1 - Where is your `.wav` file?
Upload `.wav` files to a GCS bucket if it is longer than one minute. Otherwise you can use it locally.

> This process is still manual and not covered by any script on this repo.

## Step 2 - Speech to Text GCP
Run `async.py` and you will have an `output.txt` file with the transcripted version of the `.wav` file specified in the command.

> There is a wrapper on `async.py` that identifies if the file is local or on GCS.

> Using flac files with 1 channel makes it easier to use in several cloud providers. To convert between files and have some options, use [ffmpeg](https://www.ffmpeg.org/).

``` shell
ffmpeg -i input.wav -f flac -ac 1 mono-outputput.flac
```

``` shell
python async.py <LocalPath>/file.wavORflac
python async.py gs://<BucketName>/<PathToFile>/file.wavORflac
```

> Depending if running locally or the size of the file, you many need to adjust the `timeout` setting on `async.py`. I setup for 5 minutes, by default. Also, by default, the local and GCS functions work with FLAC file.

## Step 3 - Some NLP magic
We are using the Natural Language Toolking packet on Python - [NLTK](http://www.nltk.org/). It handles well tokenization and allows you to do some very cool stuff in a very simple manner.
The file `noun-verb-counter.py` counts and outputs to terminal how many nouns and verbs on the file.

You need to have the following nltk data installed - `punkt` & `averaged_perceptron_tagger`. How can you download it? Go to your python cli and run the following (you can also add this to your python file, but this will always output something when running the python file and it *looks quite ugly*).
``` Python
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

``` shell
python noun-ver-counter.py <PathToTextFile>/textfile.txt
```

----
## TODO
- Add Unit tests
- Adjust project structure
- Add `parsed argument` to be the `output.txt` when running `async.py`
- Add support for streaming data instead of just async.