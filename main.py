from pytubefix import YouTube
from sys import argv
import os
from dotenv import load_dotenv, dotenv_values 
import argparse

def main():
	load_dotenv()
	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description="Download YT Videos",
		epilog="""
  ___________
 /           \\
|     |\     |\\
|     |/     |\|
 \___________/\|
  \\_\\_\\_\\_\\_\\_\\/
	
built by tiffanyfu""")
	parser.add_argument(
		"-v", "--video",
		action="store_true",
		# required=False,
		# type=str,
		help="add this tag to download video as mp4"
	)
	parser.add_argument(
		"-l", "--link",
		required=True,
		type=str,
		help="add URL to YouTube video, be sure to wrap in quotation marks"
	)
	args = parser.parse_args()

	print(type(args.link))
	link = args.link #argv[1]
	yt = YouTube(link)
	print(f"Downloading {yt.title}")
	
	if args.video:
		yv = yt.streams.get_highest_resolution()
		yv.download(os.getenv("DOWNLOAD_PATH"))

	ys = yt.streams.get_audio_only()
	ys.download(os.getenv("DOWNLOAD_PATH"))
	
	print(f"Complete!")

if __name__ == "__main__":
	main()
