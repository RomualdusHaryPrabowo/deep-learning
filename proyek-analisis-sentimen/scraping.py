import pandas as pd
from google_play_scraper import Sort, reviews

def scrape_playstore_reviews(app_id, target_count=12000):
    print(f"Memulai scraping untuk aplikasi: {app_id}...")
    result, continuation_token = reviews(
        app_id,
        lang='id',
        country='id',
        sort=Sort.NEWEST,
        count=target_count
    )
    
    print(f"Berhasil mengekstrak {len(result)} ulasan.")
    df = pd.DataFrame(result)
    df_filtered = df[['userName', 'score', 'at', 'content']]
    return df_filtered

if __name__ == "__main__":
    TARGET_APP = 'com.gojek.app' 
    dataset = scrape_playstore_reviews(TARGET_APP, target_count=15000)
    print(dataset.head())
    filename = f"dataset_{TARGET_APP}_15k.csv"
    dataset.to_csv(filename, index=False, encoding='utf-8')
    print(f"Dataset berhasil disimpan ke dalam file: {filename}")