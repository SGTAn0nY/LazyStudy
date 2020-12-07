import argparse
import speech_recognition as sr

print("\nLazyStudy, a simple script utilizing google's speech to text ai for students too lazy to write stuff down themselves :)\nAuthor: An0nY\nDate:   28.11.2020\n")

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--audiopath", required=True, help="Full path of the audio file to analyze")
parser.add_argument("-o", "--outpath", help="Full path where to output text file ( if not given, it will take this directory )")
parser.add_argument("-l", "--language", help="Set the language to interpret audio as, accoarding to language codes like en-US for american english ( default is de-DE (german) )")
args = vars(parser.parse_args())

print("[+] Starting ...\n")
print("[+] Arguments initialized successfully ...")

def main(args):
    if args["outpath"] == None:
        args["outpath"] = "text.txt"
    if args["language"] == None:
        args["language"] = "de-DE"
    r = sr.Recognizer()
    print("[+] Speech recognizer initialized successfully ...")
    try:
        with sr.AudioFile(args["audiopath"]) as source:
            audio = r.listen(source)
        print("[+] Audio file read successfully ...")
    except:
        print("[!] Could not listen to audio file ! Exiting !\n")
        quit()
    try:
        text = r.recognize_google(audio, language=args["language"])
        print("[+] Speech converted to text successfully ...")
    except:
        print("[!] Could not convert speech to text ! Exiting !\n")
        quit()
    try:
        with open(args["outpath"], "w+", encoding="UTF-8") as f:
            f.write(text)
        print("[+] Text written successfully to file ", args["outpath"], " ...")
    except:
        print("[!] Failed to write text to file ! Exiting !")
        quit()


main(args)