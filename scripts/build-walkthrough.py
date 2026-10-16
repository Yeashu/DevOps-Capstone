from pathlib import Path
import subprocess,json,textwrap,concurrent.futures,datetime
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[1];build=root/'.local/walkthrough-short-build';build.mkdir(exist_ok=True)
scenes=json.loads((root/'docs/recordings/orbit-capstone-walkthrough.json').read_text())['chapters']
font_root=Path('/System/Library/Fonts/Supplemental')
font=ImageFont.truetype(str(font_root/'Arial.ttf'),28)
bold=ImageFont.truetype(str(font_root/'Arial Bold.ttf'),38)
small=ImageFont.truetype(str(font_root/'Arial.ttf'),23)

def command(args):subprocess.run(args,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
def duration(path):return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(path)],text=True))
for i,s in enumerate(scenes):
 base=build/f'{i:02}';audio=base.with_suffix('.aiff');banner=base.with_suffix('.png')
 if not audio.exists():command(['say','-v','Samantha','-r','190','-o',str(audio),s['narration']])
 s['duration']=max(duration(audio)+0.3,s.get('clip',[0,0])[1]);s['index']=i
 canvas=Image.new('RGBA',(1920,1080),(0,0,0,0));draw=ImageDraw.Draw(canvas)
 draw.rectangle((0,0,1920,115),fill='#14241f');draw.rectangle((0,1000,1920,1080),fill='#14241f')
 draw.text((44,14),s['module'].upper(),font=font,fill='#b6db98');draw.text((44,52),s['title'],font=bold,fill='#eef3e9')
 label='ORIGINAL LIVE DEMO EXCERPT' if 'clip' in s else 'ACTUAL CAPTURED EVIDENCE'
 draw.text((44,1015),label+'  |  AWS resources destroyed after the recorded lifecycle',font=small,fill='#b8c8b8')
 draw.text((44,1046),'Narrated evidence walkthrough · source images and original logs are linked in README',font=small,fill='#b8c8b8')
 canvas.save(banner)
 print(f'Prepared scene {i+1}/{len(scenes)}: {s["title"]} ({s["duration"]:.1f}s)',flush=True)

def encode(s):
 i=s['index'];base=build/f'{i:02}';output=base.with_suffix('.mp4');audio=base.with_suffix('.aiff');banner=base.with_suffix('.png')
 args=['ffmpeg','-hide_banner','-loglevel','error','-y']
 if 'clip' in s:
  start,length=s['clip'];args+=['-ss',str(start),'-t',str(length),'-i',str(root/'docs/recordings/orbit-eks-rollout.mp4')]
 else:args+=['-loop','1','-framerate','15','-i',str(root/'docs/screenshots'/s['image'])]
 args+=['-i',str(audio),'-loop','1','-framerate','15','-i',str(banner)]
 crop=''
 if 'crop' in s:
  x,y,w,h=s['crop'];crop=f'crop={w}:{h}:{x}:{y},'
 vf=crop+'fps=15,scale=1840:860:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:130+(860-ih)/2:color=0x0d1914,setsar=1,tpad=stop_mode=clone:stop_duration=600'
 filters=f'[0:v]{vf}[scene];[scene][2:v]overlay=0:0:shortest=1,format=yuv420p[v];[1:a]apad=pad_dur=600[a]'
 args+=['-filter_complex',filters,'-map','[v]','-map','[a]','-t',str(s['duration']),'-c:v','libx264','-threads','2','-preset','veryfast','-crf','22','-profile:v','baseline','-level:v','4.0','-pix_fmt','yuv420p','-c:a','aac','-b:a','64k','-ac','1','-ar','44100','-movflags','+faststart',str(output)]
 if not output.exists():command(args)
 print(f'Encoded scene {i+1}/{len(scenes)}',flush=True)
 return output
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:outputs=list(pool.map(encode,scenes))
listing=build/'concat.txt';listing.write_text(''.join("file '"+str(p)+"'\n" for p in outputs))
final=root/'docs/recordings/orbit-capstone-walkthrough.mp4'
command(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(listing),'-c','copy','-movflags','+faststart',str(final)])
def stamp(seconds):
 ms=round(seconds*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02}.{ms%1000:03}'
timeline=0;vtt='WEBVTT\n\n';chapters=[]
for s in scenes:
 length=duration(build/f'{s["index"]:02}.mp4');end=timeline+length
 vtt+=f'{s["index"]+1}\n{stamp(timeline)} --> {stamp(end)}\n'+s['narration']+'\n\n'
 chapters.append({**s,'startSeconds':round(timeline,3),'endSeconds':round(end,3)})
 timeline=end
(root/'docs/recordings/orbit-capstone-walkthrough.vtt').write_text(vtt)
manifest={'assembledAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'durationSeconds':duration(final),'format':'H264 Baseline / AAC / MP4, fast start','narration':'Synthetic narration using the system Samantha voice; this is an evidence guide, not a claim of a new live AWS deployment.','provenance':'Original captured evidence images and excerpts from the original live EKS recording. AWS resources were destroyed after capture.','chapters':chapters}
(root/'docs/recordings/orbit-capstone-walkthrough.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'output':str(final),'durationSeconds':duration(final),'sizeMiB':round(final.stat().st_size/1024/1024,2),'scenes':len(scenes)}),flush=True)
