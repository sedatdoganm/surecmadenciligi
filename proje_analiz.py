import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

# 1. Veri Yükleme
dosya_yolu = '/home/sedat/Desktop/dosyaadi.csv'
df = pd.read_csv(dosya_yolu, parse_dates=['Start Time', 'End Time'])

# 2. Temel Analizler

# Toplam süre (saniye)
df['Duration'] = (df['End Time'] - df['Start Time']).dt.total_seconds()
toplam_sure_case = df.groupby('Case ID')['Duration'].sum()

print("Her Case ID'nin Toplam Süresi (saniye):")
print(toplam_sure_case)
print('\n')

# Adım frekansları
adim_frekansi = df['Activity Name'].value_counts()
print("En Sık Gerçekleşen Adımlar:")
print(adim_frekansi)
print('\n')

# Ortalama süreç tamamlama süresi
ortalama_sure = toplam_sure_case.mean()
print(f"Ortalama Süreç Tamamlanma Süresi: {ortalama_sure:.2f} saniye")
print('\n')

# Ardışık adım geçişleri
df_sorted = df.sort_values(by=['Case ID', 'Start Time'])
transitions = []

for case_id, group in df_sorted.groupby('Case ID'):
    activities = group['Activity Name'].tolist()
    for i in range(len(activities) - 1):
        transitions.append((activities[i], activities[i+1]))

transition_counts = Counter(transitions)

print("En Sık Adım Geçişleri (Adım1 -> Adım2 : Frekans):")
for (start, end), count in transition_counts.most_common():
    print(f"{start} -> {end} : {count}")

# 3. Görsel Sunum

## a) Bar Chart — Adım Frekansları
plt.figure(figsize=(8,5))
adim_frekansi.plot(kind='bar', color='skyblue')
plt.title('Adım Frekansları')
plt.xlabel('Activity Name')
plt.ylabel('Frekans')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

## b) Basit Akış Diyagramı (Directed Graph)
G = nx.DiGraph()

for (start, end), count in transition_counts.items():
    G.add_edge(start, end, weight=count)

plt.figure(figsize=(10,7))
pos = nx.spring_layout(G, seed=42)

weights = [G[u][v]['weight'] for u,v in G.edges()]
max_weight = max(weights)
edge_widths = [weight / max_weight * 5 for weight in weights]

nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1500)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edges(G, pos, width=edge_widths, arrowstyle='-|>', arrowsize=20, edge_color='gray')

plt.title('Basit Süreç Akış Diyagramı (Adım Geçişleri)')
plt.axis('off')
plt.show()
