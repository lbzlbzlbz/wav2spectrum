# -*- coding: utf-8 -*- #
import wave
import numpy
from matplotlib.pyplot import show, plot, subplot, specgram, xlabel, ylabel, magnitude_spectrum, figure, title, gca

class wavObj:
    nchannels = 0
    sampwidth = 0
    framerate = 0
    nframes = 0
    wave_data = 0

    def __init__(self, path):
        [self.nchannels, self.sampwidth, self.framerate, self.nframes, self.wave_data] = self.read_wav(path)

    def on_press(self, event):
        if event.inaxes == None:
            print "none"
            return
        self.x_start = event.xdata


    def on_release(self, event):
        if event.inaxes == None:
            print "none"
            return
        self.x_end = event.xdata
        self.plot_fd(x_start=self.x_start, x_end=self.x_end)





    # 画时域图
    def plot_td(self):
        fig = figure()
        fig.canvas.mpl_connect("button_press_event", self.on_press)
        fig.canvas.mpl_connect("button_release_event", self.on_release)
        nchannels = self.nchannels
        nframes = self.nframes
        framerate = self.framerate
        time = numpy.arange(0, nframes) * (1.0 / framerate)
        for i in range(0, nchannels):
            loc = nchannels * 100 + 10 + i + 1
            subplot(loc)
            plot(time, self.wave_data[i])
            ylabel('Magnitude(energy)')
        xlabel('Time(s)')
        return 1

    # 画语图
    def plot_sg(self, NFFT=1024):
        fig = figure()
        fig.canvas.mpl_connect("button_press_event", self.on_press)
        fig.canvas.mpl_connect("button_release_event", self.on_release)
        nchannels = self.nchannels
        framerate = self.framerate
        for i in range(0, nchannels):
            loc = nchannels * 100 + 10 + i + 1
            subplot(loc)
            specgram(self.wave_data[i], NFFT=NFFT, Fs=framerate)
            ylabel('Frequence(Hz)')
        xlabel('Time(s)')
        return 1

    #画频域图
    def plot_fd(self, x_start, x_end):
        nchannels = self.nchannels
        nframes = self.nframes
        framerate = self.framerate
        if x_start < x_end:
            time_start = self.x_start
            time_end = self.x_end
        else:
            time_start = self.x_end
            time_end = self.x_start
        data_start = int(time_start * framerate)
        data_end = int(time_end * framerate)
        print data_start, data_end
        if data_start < 0 or data_end > nframes:
            print 'exceed'
            return
        else:
            figure()
            for i in range(0, nchannels):
                loc = nchannels * 100 + 10 + i + 1
                subplot(loc)
                if i == 0:
                    fig_title = 'Time range:' + str(round(time_start,2)) + 's to ' + str(round(time_end,2)) + 's';
                    title(fig_title)
                wava_data_onechannel = self.wave_data[i][data_start:data_end]
                magnitude_spectrum(wava_data_onechannel, Fs=framerate, sides='default', scale='dB')
            show()

    #读取wav文件
    def read_wav(self, path):
        try:
            wave_file = wave.open(path, 'r')
            params = wave_file.getparams()
            nchannels, sampwidth, framerate, nframes = params[:4]
            wave_data = numpy.fromstring(wave_file.readframes(nframes), dtype=numpy.short)
            wave_file.close()
            wave_data.shape = -1, nchannels
            return nchannels, sampwidth, framerate, nframes, wave_data.T
        except:
            nchannels = 0
            sampwidth = 0
            framerate = 0
            nframes = 0
            wave_data = 0
            return nchannels, sampwidth, framerate, nframes, wave_data

    #显示figure
    def show(self):
        show()
