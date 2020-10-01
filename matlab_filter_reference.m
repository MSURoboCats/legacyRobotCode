clear;
close all;
clc;
filepath = fullfile ('rosbags','2019-11-15-15-24-56.bag');
bagselect = rosbag(filepath);
bagselect1 = select(bagselect, 'Topic', '/imu/data');
ts = timeseries(bagselect1,'LinearAcceleration.Y');
ts.data;
% meandata = mean(ts.data);
% detrend = ts.data - meandata;
figure()
plot(ts.data);
h = findobj(gca,'Type','line');
x=get(h,'Xdata');
y=get(h,'Ydata');
D.acc = y;
acc = D.acc;
Fs = 100;
Fn = Fs/2;
Ts = 1/Fs;
L = length(acc);
t = linspace(0, L, L)*Ts;
figure(1)
plot(t, acc)
grid
Facc = fft(acc)/L;
Fv = linspace(0, 1, fix(L/2)+1)*Fn;
Iv = 1:length(Fv);
figure(2)
semilogx(Fv, abs(Facc(Iv))*2)
grid
Wp = 1/Fn;                                              % Passband Frequencies (Normalised)
Ws = 1.1/Fn;                                            % Stopband Frequencies (Normalised)
Rp = 10;                                                % Passband Ripple (dB)
Rs = 50;                                                % Stopband Ripple (dB)
[n,Ws] = cheb2ord(Wp,Ws,Rp,Rs);                         % Filter Order
[z,p,k] = cheby2(n,Rs,Ws);                              % Filter Design
[sosbp,gbp] = zp2sos(z,p,k);                            % Convert To Second-Order-Section For Stability
figure(3)
freqz(sosbp, 2^16, Fs)                                  % Filter Bode Plot
s_filt = filtfilt(sosbp,gbp, acc);                      % Filter Signal
figure(4)
plot(t, acc, '-b')
hold on
plot(t, s_filt, '-r', 'LineWidth',1.5)
hold off
xlabel('Time')
ylabel('Amplitude')
legend('Original', 'Lowpass Filtered')
velocity = cumtrapz(t-1,s_filt);
position = trapz(t-1,velocity);
figure()
plot(t,velocity)
velocity1 = cumtrapz(x,s_filt);
position1 = trapz(x,velocity1);


% 
% N = 259;
% fs = 100;
% fax_bins = [0 : N-1]; %N is the number of samples in the signal
% figure()
% plot(fax_bins, abs(fft(signal)))
% xlabel('Frequency (Bins)')
% ylabel('Magnitude');
% title('Double-sided Magnitude spectrum (bins)');
% axis tight
% %
% X_mags = abs(fft(signal));
% fax_bins = [0 : N-1]; %frequency axis in bins
% N_2 = ceil(N/2);
% plot(fax_bins(1:N_2), X_mags(1:N_2))
% xlabel('Frequency (Bins)')
% ylabel('Magnitude');
% title('Single-sided Magnitude spectrum (bins)');
% axis tight
% %%
% X_mags = abs(fft(signal));
% bin_vals = [0 : N-1];
% fax_Hz = bin_vals*fs/N;
% N_2 = ceil(N/2);
% plot(fax_Hz(1:N_2), X_mags(1:N_2))
% xlabel('Frequency (Hz)')
% ylabel('Magnitude');
% title('Single-sided Magnitude spectrum (Hertz)');
% axis tight
% %%
% X_mags = abs(fft(signal));
% bin_vals = [0 : N-1];
% fax_Hz = bin_vals*fs/N;
% N_2 = ceil(N/2);
% plot(fax_Hz(1:N_2), 10*log10(X_mags(1:N_2)))
% xlabel('Frequency (Hz)')
% ylabel('Magnitude (dB)');
% title('Single-sided Magnitude spectrum (Hertz)');
% axis tight
% 
% 
% % velocity=cumtrapz(x,y)
% % plot(velocity);
% % position=trapz(x,velocity)
% % velocitynew = velocity - mean(velocity)
% % figure()
% % plot(velocitynew)
% % % detrendvelocitynew = detrend(velocitynew)
% % % plot(x,detrendvelocitynew)
% % position=cumtrapz(x,velocitynew)
% % positionnew=position-mean(position)
% % positionfinal=trapz(x,positionnew)
% % %window = 1000;
% % % overlap = round(0.9*window);
% % s = spectrogram(y,window,noverlap)
% % 
% %detrend(x,y);
% %plot(detrend)
% velocity=cumtrapz(x,y);
% position=trapz(x,velocity);
