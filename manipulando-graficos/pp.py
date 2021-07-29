import plotly.express as px

x = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago']
y = ['12', '5', '20', '4', '9', '11', '15', '19']

# Usando o gráfico linha
fig = px.line(x=x, y=y)

fig.update_yaxes(title='Pontos', title_font_color='red')
fig.update_xaxes(title='Posição', title_font_color='blue')

# Exibe o gráfico no browser
fig.show()
