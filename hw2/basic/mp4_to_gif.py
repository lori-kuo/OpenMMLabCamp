import moviepy.editor as mp

clip = mp.VideoFileClip("./color_splash_result.mp4")
clip.write_gif("output.gif",fps=10)