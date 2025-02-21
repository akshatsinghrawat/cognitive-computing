df=pd.read_csv('/content/drive/MyDrive/company_sales_data.csv')
df

plt.figure(figsize=(10,5))
plt.plot(df['month_number'],df['total_profit'],color='green',linestyle='-',linewidth=2)
plt.grid()
plt.xlabel('month number',color='black')
plt.ylabel('profits',color='black')
plt.legend()
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df['month_number'],df['facecream'],color='green',linestyle='-',linewidth=2,label='facecream')
plt.plot(df['month_number'],df['toothpaste'],color='orange',linestyle='-',linewidth=2,label='toothpaste')
plt.plot(df['month_number'],df['bathingsoap'],color='red',linestyle='-',linewidth=2,label='bathingsoap')
plt.plot(df['month_number'],df['shampoo'],color='blue',linestyle='-',linewidth=2,label='shampoo')
plt.plot(df['month_number'],df['moisturizer'],color='black',linestyle='-',linewidth=2,label='moisturizer')
plt.legend()
plt.grid()
plt.show()


df.set_index('month_number', inplace=True)
df.drop('total_profit',axis=1,inplace=True)

df.plot(kind='bar', figsize=(10, 6), colormap='viridis')

plt.xlabel('Month Number')
plt.ylabel('Values')
plt.title('Monthly Sales Data')
plt.legend(title="Attributes")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
     