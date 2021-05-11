from matplotlib.ticker import PercentFormatter

def pareto_chart(df_, Column):
    df = pd.DataFrame({Column:df_[Column].value_counts().index.astype(str).tolist(), 'Count':df_[Column].value_counts().tolist()})
    df['Percentage'] = df['Count'].cumsum()/df['Count'].sum()*100

    fig, ax = plt.subplots(figsize=(20,5))
    ax.bar(df[Column], df['Count'], color='C0')
    ax2 = ax.twinx()
    ax2.plot(df[Column], df['Percentage'], color='C1', marker=".")
    ax2.yaxis.set_major_formatter(PercentFormatter())

    ax.tick_params(axis="y", colors="C0")
    ax.tick_params(axis="y", colors="C1")

    for tick in ax.get_xticklabels():
        # Setting the X category angle of adjustment
        tick.set_rotation(45)
    plt.show()