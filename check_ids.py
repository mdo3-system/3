with open('video_production_portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = [
    'veo3StoryTitleHeader', 'veo3ClipsGrid', 'currentGradeTitle', 'videoSource',
    'vocabStoryTitle', 'vocabTableBody', 'yt_live_url_input', 'yt_all_grade_slots_grid',
    'yt_field_title', 'yt_field_desc', 'yt_field_tags', 'yt_field_pinned',
    'yt_video_folder_path', 'yt_download_links_bar', 'sync_yt_url_link',
    'note_field_title', 'note_field_body', 'note_field_tags', 'note_image_preview',
    'note_image_download_btn', 'note_img_path_text', 'x_field_t1', 'x_field_t2',
    'x_field_t3', 'xDirectTweetBtn', 'ig_field_caption'
]

missing = [i for i in ids if f'id="{i}"' not in html and f"id='{i}'" not in html]
print("Missing IDs:", missing)
