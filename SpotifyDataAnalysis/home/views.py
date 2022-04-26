from django.shortcuts import render
from .forms import SongFrom
from .dash_apps.finished_apps import simplexample
from django.views.decorators.csrf import csrf_exempt
from plotly.offline import plot
from plotly.graph_objs import Scatter


# Create your views here.
def home(request):
    x_data ,y_data,df =simplexample.argentina()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/welcome.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})
#'energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms'
@csrf_exempt
def predict(requests):
    form=SongFrom()
    context={'form':form}
    return render(requests, 'home/predict.html',context)

def australia(request):
    x_data ,y_data,df =simplexample.australia()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/Australia.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})

def england(request):
    x_data ,y_data,df =simplexample.england()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/england.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})


def usa(request):
    x_data ,y_data,df =simplexample.usa()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/USA.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})

def mexico(request):
    x_data ,y_data,df =simplexample.mexico()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/Mexico.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})
def Spain(request):
    x_data ,y_data,df =simplexample.spain()

    plot_dance = plot([Scatter(x=x_data[0], y=df[y_data[0]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    plot_energy = plot([Scatter(x=x_data[1], y=df[y_data[1]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_key = plot([Scatter(x=x_data[2], y=df[y_data[2]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_loudness = plot([Scatter(x=x_data[3], y=df[y_data[3]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_mode = plot([Scatter(x=x_data[4], y=df[y_data[4]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')


    plot_speechiness = plot([Scatter(x=x_data[5], y=df[y_data[5]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')



    plot_acousticness = plot([Scatter(x=x_data[6], y=df[y_data[6]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_instrumentalness = plot([Scatter(x=x_data[7], y=df[y_data[7]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    
    plot_liveness = plot([Scatter(x=x_data[8], y=df[y_data[8]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_valence = plot([Scatter(x=x_data[9], y=df[y_data[9]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_tempo = plot([Scatter(x=x_data[10], y=df[y_data[10]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    plot_duration_ms = plot([Scatter(x=x_data[11], y=df[y_data[11]],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
               
    return render(request,'home/Spain.html',context={'p_d': plot_dance, 'p_e':plot_energy,'p_k':plot_key,'p_l':plot_loudness, 'p_m':plot_mode,'p_s':plot_speechiness , 'p_a':plot_acousticness, 'p_i':plot_instrumentalness,'p_li':plot_liveness,'p_v':plot_valence,'p_t':plot_tempo,'p_d':plot_duration_ms})



