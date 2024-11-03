from pathlib import Path

output_dir = Path("output_dir")
files = ['part-00000', 'part-00001']
user_ids, urls = [], []
max_n_ps, max_n_visits = 0, 0

for file in files:
    with open(output_dir / file) as f:
        user_id, n_ps = f.readline().strip().split('\t')
        url, n_visits = f.readline().strip().split('\t')
        n_ps, n_visits = int(n_ps), int(n_visits)
        
        if n_ps > max_n_ps:
            user_ids = [user_id]
            max_n_ps = n_ps
        elif n_ps == max_n_ps:
            user_ids.append(user_id)
        
        if n_visits > max_n_visits:
            urls = [url]
            max_n_visits = n_visits
        elif n_visits == max_n_visits:
            urls.append(url)

print("User id(s) with the most number of accesses to .ps files:")
for user in user_ids:
    print(f"- {user}")
print(f"Total accesses: {max_n_ps}\n")

print("Url(s) with the most number of visitors:")
for url in urls:
    print(f"- {url}")
print(f"Total visits: {max_n_visits}")
