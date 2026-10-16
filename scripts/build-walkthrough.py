from pathlib import Path
import subprocess,json,textwrap,concurrent.futures,datetime
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[1];build=root/'.local/walkthrough-silent-build';build.mkdir(exist_ok=True)
scenes=json.loads((root/'docs/recordings/presentation.json').read_text())['chapters']
font_root=Path('/System/Library/Fonts/Supplemental')
font=ImageFont.truetype(str(font_root/'Arial.ttf'),28)
bold=ImageFont.truetype(str(font_root/'Arial Bold.ttf'),38)
small=ImageFont.truetype(str(font_root/'Arial.ttf'),23)

def command(args):subprocess.run(args,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
def duration(path):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(path)],text=True))
for i,s in enumerate(scenes):
 base=build/f'{i:02}';banner=base.with_suffix('.png')
 s['duration']=max(s['duration'],s.get('clip',[0,0])[1]);s['index']=i
 canvas=Image.new('RGBA',(1920,1080),(0,0,0,0));draw=ImageDraw.Draw(canvas)
 draw.rectangle((0,0,1920,115),fill='#14241f');draw.rectangle((0,1000,1920,1080),fill='#14241f')
 draw.text((44,14),s['module'].upper(),font=font,fill='#b6db98');draw.text((44,52),s['title'],font=bold,fill='#eef3e9')
 label='ORIGINAL LIVE DEMO EXCERPT' if 'clip' in s else 'ACTUAL CAPTURED EVIDENCE'
 draw.text((44,1007),label+' · AWS resources destroyed after capture',font=small,fill='#b8c8b8')
 draw.text((44,1040),s['subtitle'],font=font,fill='#eef3e9')
 canvas.save(banner)
 print(f'Prepared scene {i+1}/{len(scenes)}: {s["title"]} ({s["duration"]:.1f}s)',flush=True)

def encode(s):
 i=s['index'];base=build/f'{i:02}';output=base.with_suffix('.mp4');banner=base.with_suffix('.png')
 args=['ffmpeg','-hide_banner','-loglevel','error','-y']
 if 'clip' in s:
  start,length=s['clip'];args+=['-ss',str(start),'-t',str(length),'-i',str(root/'docs/recordings/orbit-eks-rollout.mp4')]
 else:args+=['-loop','1','-framerate','15','-i',str(root/'docs/screenshots'/s['image'])]
 args+=['-loop','1','-framerate','15','-i',str(banner)]
 crop=''
 if 'crop' in s:
  x,y,w,h=s['crop'];crop=f'crop={w}:{h}:{x}:{y},'
 vf=crop+'fps=15,scale=1840:860:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:130+(860-ih)/2:color=0x0d1914,setsar=1,tpad=stop_mode=clone:stop_duration=600'
 filters=f'[0:v]{vf}[scene];[scene][1:v]overlay=0:0:shortest=1,format=yuv420p[v]'
 args+=['-filter_complex',filters,'-map','[v]','-an','-t',str(s['duration']),'-c:v','libx264','-threads','2','-preset','veryfast','-crf','22','-profile:v','baseline','-level:v','4.0','-pix_fmt','yuv420p','-movflags','+faststart',str(output)]
 if not output.exists():command(args)
 print(f'Encoded scene {i+1}/{len(scenes)}',flush=True)
 return output
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:outputs=list(pool.map(encode,scenes))
listing=build/'concat.txt';listing.write_text(''.join("file '"+str(p)+"'\n" for p in outputs))
final=root/'docs/recordings/presentation.mp4'
# Normalize the joined segments into one stream so Firefox seeks to fresh frames.
command(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(listing),'-vf','fps=25,setpts=PTS-STARTPTS','-an','-c:v','libx264','-threads','2','-preset','veryfast','-crf','23','-profile:v','baseline','-level:v','4.0','-pix_fmt','yuv420p','-g','50','-keyint_min','50','-sc_threshold','0','-movflags','+faststart',str(final)])
def stamp(seconds):
 ms=round(seconds*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}.{ms%1000:03}'
timeline=0;vtt='WEBVTT\n\n';chapters=[]
for s in scenes:
 length=duration(build/f'{s["index"]:02}.mp4');end=timeline+length
 vtt+=f'{s["index"]+1}\n{stamp(timeline)} --> {stamp(end)}\n'+s['subtitle']+'\n\n'
 chapters.append({**s,'startSeconds':round(timeline,3),'endSeconds':round(end,3)})
 timeline=end
(root/'docs/recordings/presentation.vtt').write_text(vtt)
manifest={'assembledAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'durationSeconds':duration(final),'format':'H264 Baseline / MP4, fast start; no audio track','subtitles':'Brief on-screen labels; optional matching WebVTT track.','provenance':'Original captured evidence images and excerpts from the original live EKS recording. AWS resources were destroyed after capture.','chapters':chapters}
(root/'docs/recordings/presentation.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'output':str(final),'durationSeconds':duration(final),'sizeMiB':round(final.stat().st_size/1024/1024,2),'scenes':len(scenes)}),flush=True)
