import asyncio
import os
import re
import sys
import glob
import subprocess
import edge_tts

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = r"d:\Dropbox\■設計ｻﾎﾟｰﾄ\■note\antigravity\kindle"
OUTPUT_BASE = os.path.join(BASE_DIR, "video_output")
INBOX_DIR = os.path.join(BASE_DIR, "veo3_inbox")
CHAPTER_DIR = os.path.join(OUTPUT_BASE, "chapter01_tortoise_and_hare")

os.makedirs(CHAPTER_DIR, exist_ok=True)

# 6つのバージョン（4級、3級、準2級、2級、準1級、クラシック原文）
ALL_GRADES_TEXTS = [
    {
        "grade_key": "Grade_4",
        "level_label": "Eiken Grade 4 (英検4級)",
        "voice": "en-US-GuyNeural",
        "rate": "-6%",
        "text": (
            "A proud hare always laughed at a slow tortoise. "
            '"You walk so slowly! Look at me. I am the fastest animal in the forest," the hare said. '
            'The tortoise smiled and answered, "Let\'s have a race today. I can run faster than you think." '
            'The hare laughed loudly. "That is impossible! But okay, let\'s run." '
            'The race started. The hare ran very fast. Soon, he was far ahead of the tortoise. '
            'He looked back and saw no one. "The tortoise is too slow. I have a lot of time. '
            'I will take a short nap under this big tree," said the hare. He sat down and fell asleep. '
            'Meanwhile, the tortoise kept walking. He did not stop. He walked step by step. '
            'When the hare woke up, the sun was going down. He ran quickly to the finish line. '
            'However, the tortoise was already there! '
            'Slow and steady wins the race.'
        )
    },
    {
        "grade_key": "Grade_3",
        "level_label": "Eiken Grade 3 (英検3級)",
        "voice": "en-US-ChristopherNeural",
        "rate": "-3%",
        "text": (
            "Once upon a time, a proud hare was always boasting about his speed to the other animals. "
            'He especially enjoyed making fun of a slow tortoise. "Nobody can beat me because I am the fastest runner in these woods!" he cried. '
            'To his surprise, the quiet tortoise replied calmly, "I accept your challenge. Let\'s race to the top of the hill." '
            'The hare laughed out loud, believing that victory was already his. As soon as the signal was given, the hare dashed forward and left the tortoise far behind. '
            'After running for a while, the hare stopped to look back. The tortoise was moving so slowly that he was barely visible in the distance. '
            '"I have plenty of time before he catches up," thought the hare. "I think I will rest under this shady tree." He lay down on the soft grass and soon fell into a deep sleep. '
            'While the hare was sleeping, the tortoise continued to walk steadily without stopping. '
            'When the hare finally opened his eyes, he saw that the sun was setting. He sprinted toward the finish line as fast as he could. '
            'However, the tortoise had already crossed the line and won the race. '
            'Persistence and hard work will always bring success in the end.'
        )
    },
    {
        "grade_key": "Grade_Pre2",
        "level_label": "Eiken Grade Pre-2 (英検準2級)",
        "voice": "en-US-GuyNeural",
        "rate": "+0%",
        "text": (
            "An arrogant hare was constantly boasting of his extraordinary speed to all the forest creatures. "
            'He took particular pleasure in mocking a slow-moving tortoise. "I challenge anyone in these woods to a race," the hare proclaimed arrogantly. '
            '"No one has ever defeated me, nor will anyone ever succeed!" '
            'Much to the hare\'s astonishment, the quiet tortoise stepped forward and replied with composure, "I accept your challenge. Let us compete to see who reaches the summit of the hill first." '
            'Amused by the proposal, the hare agreed immediately, confident of an easy victory. The moment the competition began, the hare accelerated rapidly, leaving his opponent far behind in a cloud of dust. '
            'Upon reaching the midpoint of the course, the hare glanced back and noticed that the tortoise was barely visible in the remote distance. '
            '"It will take him hours to catch up with me," reasoned the hare. "Therefore, I can comfortably enjoy a refreshing nap beneath the oak tree." '
            'Feeling thoroughly relaxed, he lay down in the shade and fell into a profound slumber. '
            'Meanwhile, the tortoise maintained a slow but steady pace, advancing continuously without a single moment of hesitation. '
            'By the time the hare finally awoke, twilight had descended upon the forest. Realizing his grave mistake, he sprinted toward the finish line with all his remaining strength. '
            'To his utter dismay, however, the tortoise had already crossed the goal and secured a triumphant victory. '
            'Sloth and overconfidence lead to ruin, whereas steady perseverance ultimately triumphs over natural talent.'
        )
    },
    {
        "grade_key": "Grade_2",
        "level_label": "Eiken Grade 2 (英検2級)",
        "voice": "en-US-ChristopherNeural",
        "rate": "+2%",
        "text": (
            "A notoriously boastful hare perpetually ridiculed the sluggish movement of a tortoise, repeatedly asserting his own unexcelled swiftness before the woodland community. "
            '"Regardless of who dares to challenge me," declared the hare with supreme arrogance, "my natural velocity remains entirely insurmountable." '
            'Unfazed by the hare\'s pompous declaration, the tortoise calmly offered a counter-proposal. '
            '"Notwithstanding your remarkable speed, I am prepared to engage in a competitive race to the designated hilltop." '
            'Deeming the challenge absurdly amusing, the hare readily accepted, anticipating an inevitable triumph. '
            'At the commencement of the race, the hare burst forward with extraordinary acceleration, swiftly establishing a formidable lead that rendered his competitor virtually invisible. '
            'Having traversed half the distance in mere minutes, the hare paused to assess his progress. Perceiving that the tortoise was lagging far behind, the hare succumbed to complacency. '
            '"Inasmuch as the gap between us is immense," he calculated, "a temporary respite will in no way compromise my impending victory." '
            'Consequently, he reclined beneath the dense foliage of a venerable oak and lapsed into an unalterable sleep. '
            'In sharp contrast, the tortoise exhibited unwavering determination. Advancing with relentless continuity, he traversed the rugged terrain without succumbing to fatigue or distraction. '
            'When the hare eventually awakened, nightfall was imminently approaching. Panic-stricken upon discovering the tortoise\'s proximity to the finish line, the hare exerted his maximum capacity in a desperate pursuit. '
            'Nevertheless, his delayed effort proved futile; the tortoise had already crossed the boundary, securing an unprecedented triumph. '
            'Indolence and unwarranted self-assurance inevitably culminate in failure, whereas relentless perseverance consistently surpasses raw talent.'
        )
    },
    {
        "grade_key": "Grade_Pre1",
        "level_label": "Eiken Grade Pre-1 (英検準1級)",
        "voice": "en-US-GuyNeural",
        "rate": "+4%",
        "text": (
            "An ostentatious hare habitually demeaned the sluggish gait of a tortoise, relentlessly proclaiming his own athletic preeminence to the forest fauna. "
            '"Should any creature presume to contest my velocity," the hare boasted with pompous disdain, "such an endeavor is preordained to fail, for my swiftness is fundamentally unassailable." '
            'Impervious to the hare\'s supercilious bravado, the tortoise articulated a measured proposition. '
            '"Notwithstanding your heralded agility, I hereby challenge you to a footrace terminating at the mountain summit." '
            'Deriding the proposal as a preposterous delusion, the hare acquiesced with patronizing enthusiasm. '
            'Upon the signal, the hare bounded forth with phenomenal momentum, establishing a colossal chasm between himself and his adversary within seconds. '
            'Having covered half the course, the hare paused to survey the distance. Observing the tortoise far in the rear, the hare succumbed to fatalistic complacency. '
            '"Given the insurmountable magnitude of my lead," he rationalized, "a brief interlude of slumber shall not jeopardize my triumph." '
            'Whereupon, he sought refuge beneath a canopy of leaves and lapsed into a profound coma. '
            'Conversely, the tortoise displayed unyielding tenacity. Maintaining an unhurried yet unrelenting cadence, he negotiated the treacherous incline without a single moment of hesitation. '
            'By the time the hare emerged from his torpor, twilight had enveloped the horizon. Espying his rival adjacent to the finish line, the hare sprinted with frenecy; '
            'nevertheless, his belated surge proved entirely ineffectual. The tortoise had already crossed the threshold, achieving an historic victory. '
            'Haughty indolence and premature triumph subvert inherent superiority, whereas steadfast tenacity inexorably eclipses uncultivated genius.'
        )
    },
    {
        "grade_key": "Classic_Original",
        "level_label": "Classic Original Text (クラシック原文)",
        "voice": "en-GB-RyanNeural", # クラシックな格調高いイギリス英語ナレーション
        "rate": "-2%",
        "text": (
            "A Hare was one day making fun of the short feet and slow pace of the Tortoise, who retorted: "
            '"Though you be swift as the wind, I will beat you in a race." '
            "The Hare, believing her assertion to be simply impossible, agreed to the proposal; "
            "and they agreed that the Fox should choose the course and fix the goal. "
            "On the day appointed for the race the two started together. "
            "The Tortoise never for a moment stopped, but went on with a slow but steady pace straight to the end of the course. "
            "The Hare, lying down by the wayside, fell asleep. "
            "At last waking up, and moving as fast as he could, he saw the Tortoise had reached the goal, "
            "and was comfortably resting after her fatigue. "
            "Slow and steady wins the race."
        )
    }
]

def format_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    centis = int(round((seconds - int(seconds)) * 100))
    if centis >= 100: centis = 99
    return f"{hours:01d}:{minutes:02d}:{secs:02d}.{centis:02d}"

async def render_grade(item, clip1, clip2, clip3):
    grade_key = item["grade_key"]
    level_label = item["level_label"]
    voice = item["voice"]
    rate = item["rate"]
    text = item["text"]
    
    print(f"\n--- 🚀 生成中: {level_label} ---")
    
    audio_path = os.path.join(CHAPTER_DIR, f"narration_{grade_key}.mp3")
    ass_path = os.path.join(CHAPTER_DIR, f"karaoke_{grade_key}.ass")
    out_video = os.path.join(CHAPTER_DIR, f"chapter01_{grade_key}.mp4")
    
    # 1. 音声生成
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    sentence_timings = []
    with open(audio_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "SentenceBoundary":
                offset_sec = chunk["offset"] / 10_000_000
                duration_sec = chunk["duration"] / 10_000_000
                sentence_timings.append({
                    "text": chunk["text"],
                    "start": offset_sec,
                    "end": offset_sec + duration_sec,
                    "duration": duration_sec
                })
                
    total_audio_duration = sentence_timings[-1]["end"] + 1.2 if sentence_timings else 60.0
    print(f"   [1/2] 音声生成完了 ({total_audio_duration:.1f} 秒)")
    
    # 2. 字幕生成
    ass_content = f"""[Script Info]
Title: Chapter 1 The Tortoise and the Hare - {level_label}
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: HeaderTitle,Arial,34,&H00FFFFFF,&H00000000,&H00000000,&H80000000,-1,0,0,0,100,100,1,0,1,2,0,8,60,60,35,1
Style: KaraokeEnglish,Arial,50,&H00FFFFFF,&H0000E5FF,&H00000000,&H90000000,-1,0,0,0,100,100,2,0,1,4,2,2,100,100,75,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ass_content += f"Dialogue: 0,0:00:00.00,{format_ass_time(total_audio_duration)},HeaderTitle,,0,0,0,,{{\\fad(400,400)}}📖 Chapter 01: The Tortoise and the Hare (ウサギとカメ)  |  {level_label}\n"
    
    for timing in sentence_timings:
        start_sec = max(0.0, timing["start"])
        end_sec = timing["end"] + 0.3
        words = timing["text"].split()
        if not words: continue
        
        total_chars = sum(max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w))) for w in words)
        total_duration_csec = max(len(words), int(round(timing["duration"] * 100)))
        
        k_text = ""
        for w in words:
            clean_len = max(1, len(re.sub(r'[^a-zA-Z0-9]', '', w)))
            w_csec = max(1, int(round((clean_len / total_chars) * total_duration_csec)))
            k_text += f"{{\\k{w_csec}}}{w} "
            
        ass_content += f"Dialogue: 1,{format_ass_time(start_sec)},{format_ass_time(end_sec)},KaraokeEnglish,,0,0,0,,{{\\fad(150,150)}}{k_text.strip()}\n"
        
    with open(ass_path, "w", encoding="utf-8") as f:
        f.write(ass_content)
        
    # 3. 3本のVeo動画を音声の長さに合わせて自動フィット（タイムストレッチ）
    dur1 = total_audio_duration * 0.35
    dur2 = total_audio_duration * 0.35
    dur3 = total_audio_duration - (dur1 + dur2) + 0.5
    
    ass_escaped = ass_path.replace("\\", "/").replace(":", "\\:")
    
    pts1 = max(1.0, dur1 / 10.0)
    pts2 = max(1.0, dur2 / 10.0)
    pts3 = max(1.0, dur3 / 10.0)
    
    filter_complex = (
        f"[0:v]setpts={pts1:.2f}*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur1:.2f}[v0];"
        f"[1:v]setpts={pts2:.2f}*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur2:.2f}[v1];"
        f"[2:v]setpts={pts3:.2f}*PTS,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,trim=duration={dur3:.2f}[v2];"
        f"[v0][v1][v2]concat=n=3:v=1:a=0[vcat];"
        f"[vcat]drawbox=y=0:color=black@0.7:width=iw:height=90:t=fill,"
        f"drawbox=y=ih-180:color=black@0.78:width=iw:height=180:t=fill,"
        f"ass='{ass_escaped}'[v]"
    )

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", clip1,
        "-i", clip2,
        "-i", clip3,
        "-i", audio_path,
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-map", "3:a",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        out_video
    ]
    
    print(f"   [2/2] FFmpeg 合成中 (目標尺: {total_audio_duration:.1f} 秒)...")
    res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"   ✅ 完成: {out_video}")
    else:
        print(f"   ❌ エラー: {res.stderr}")

async def main():
    inbox_files = sorted(glob.glob(os.path.join(INBOX_DIR, "*.mp4")))
    if len(inbox_files) < 3:
        print("❌ Veo動画が3本揃っていません")
        return
        
    clip1, clip2, clip3 = inbox_files[0], inbox_files[1], inbox_files[2]
    
    for item in ALL_GRADES_TEXTS:
        await render_grade(item, clip1, clip2, clip3)
        
    print("\n🎉 クラシック原文版を含む全6バリエーションの動画生成がすべて完了しました！")

if __name__ == "__main__":
    asyncio.run(main())
