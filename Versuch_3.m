%% Versuch 3 Digitale Signalübertragung

clear all 
clc

[x, fs1] = audioread('C:\Users\marvi\Studium\Semester 6\Digitale Signalübertragung\Versuche\Audiodaten\itu_female1.wav');
[y, fs2] = audioread('C:\Users\marvi\Studium\Semester 6\Digitale Signalübertragung\Versuche\Audiodaten\itu_male1.wav');


figure(1)
spectrogram(x,512,256,512,fs1);
figure(2)
spectrogram(y,512,256,512,fs2);

%Trägerfrequenz 20kHz
f0 = 20000;
fs = 8*fs1;


uberabtast = upsample(x,8);
uberabtast1 = upsample(y,8);


[b,a]= butter(5,0.9*0.125);
figure(3)
freqz(b,a)

imag_x = filter(b,a,uberabtast);
real_x = filter(b,a,uberabtast1);


T = length(real_x) * 1/fs;
t = linspace(0,T,length(real_x))';

s0_re = cos(2*pi*f0*t);
s0_im = sin(2*pi*f0*t);

s2 = real_x .* s0_re - imag_x .* s0_im;
figure(4)
spectrogram(s2,512,256,512,8*fs1)