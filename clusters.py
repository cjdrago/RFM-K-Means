# Disactive plot using plotly
import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

scaled_df = pd.read_csv('../onlineRetail/onlineRetail_Scaled.csv', sep = ',', header = 0)
grouped_df = pd.read_csv('../onlineRetail/grouped_df.csv', sep = ',', header = 0)

print(scaled_df)
print(grouped_df)

kmeans = KMeans(n_clusters=3, max_iter=300)
kmeans.fit(scaled_df)

# centroids = kmeans.cluster_centers_
# scaled_df['Cluster'] = kmeans.labels_
# scaled_df['CustomerID'] = grouped_df['CustomerID']

# fig = px.scatter_3d(scaled_df, x = 'amount', y = 'Frequency', z ='transactionRecency',
#                     hover_data=['CustomerID'],  color='Cluster', opacity=0.8)

# fig.update_traces(mode='markers', marker_size=4)
# fig.show()
