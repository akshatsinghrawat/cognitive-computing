arr=np.array([1,2,3,6,4,5])
print(arr[::-1])
def most_freq(arr):
  unique,counts=np.unique(arr,return_counts=True)
  n=max(counts)
  val=unique[counts==n][0]
  print(f'most frequent value is {val}')
  for i in range(len(arr)):
    if arr[i]==val:
      print(i,end="")
  print("")
x=np.array([1,2,3,4,5,1,2,1,1,1])
most_freq(x)
y=np.array([1,1,1,2,3,4,2,4,3,3])
most_freq(y)