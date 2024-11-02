from pathlib import Path

output_dir = Path("output_dir")
sources_dir = Path("sources")
files = ['part-00000', 'part-00001']
user_ids, n_ps, urls, n_visits = [], None, [], None

for file in files:
    with open(output_dir / file) as f:
        current_user_id, current_n_ps = f.readline().strip().split('\t')
        current_url, current_n_visits = f.readline().strip().split('\t')
        current_n_ps = int(current_n_ps)
        current_n_visits = int(current_n_visits)
        
        if n_ps is None or current_n_ps > n_ps:
            user_ids = [current_user_id]
            n_ps = current_n_ps
        elif current_n_ps == n_ps:
            user_ids.append(current_user_id)

        if n_visits is None or current_n_visits > n_visits:
            urls = [current_url]
            n_visits = current_n_visits
        elif current_n_visits == n_visits:
            urls.append(current_url)

print(f"User id(s) with most number of accesses to .ps files:")
for user in user_ids:
    print(f"- {user}")
print(f"Total accesses: {n_ps}")

print()

print("Url(s) with the most number of visitors:")
for url in urls:
    print(f"- {url}")
print(f"Total visits: {n_visits}")
