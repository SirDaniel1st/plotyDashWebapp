from django.shortcuts import render
from .forms import SongFrom
from .dash_apps.finished_apps import simplexample
from django.views.decorators.csrf import csrf_exempt
from plotly.offline import plot
from plotly.graph_objs import Scatter

def plotter(request,path,x_data ,y_data,df):
    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],mode='lines', name='test',opacity=0.8, marker_color='red')],output_type='div')
    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],mode='lines', name='test',opacity=0.8, marker_color='green')],output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],mode='lines', name='test',opacity=0.8, marker_color='blue')],output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],mode='lines', name='test',opacity=0.8, marker_color='orange')],output_type='div')
    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],mode='lines', name='test',opacity=0.8, marker_color='purple')],output_type='div')
    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],mode='lines', name='test',opacity=0.8, marker_color='yellow')],output_type='div')
    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],mode='lines', name='test',opacity=0.8, marker_color='cyan')],output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],mode='lines', name='test',opacity=0.8, marker_color='pink')],output_type='div')
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],mode='lines', name='test',opacity=0.8, marker_color='black')],output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],mode='lines', name='test',opacity=0.8, marker_color='brown')],output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],mode='lines', name='test',opacity=0.8, marker_color='teal')],output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],mode='lines', name='test',opacity=0.8, marker_color='green')],output_type='div')
    context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_du':plot_duration_ms}
    return context

def home(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/argentina.csv'
    path='home/welcome.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

def australia(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/Australia.csv'
    path='home/Australia.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

def england(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/England.csv'
    path='home/England.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

def usa(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/USA.csv'
    path='home/USA.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

def mexico(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/Mexico.csv'
    path='home/Mexico.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

def spain(request):
    filepath='/workspace/plotyDashWebapp/SpotifyDataAnalysis/home/dash_apps/finished_apps/CSVFile/Spain.csv'
    path='home/Spain.html'
    x_data ,y_data,df =simplexample.Top100(filepath)
    context=plotter(request,path,x_data,y_data,df)
    return render(request,path,context)

@csrf_exempt
def predict(requests):
    form=SongFrom()
    context={'form':form}
    return render(requests, 'home/predict.html',context)