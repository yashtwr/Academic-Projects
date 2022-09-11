clc;
close all;
n = 512;
s = 30;
v = 128;
x_initial = zeros(n,1);

% Original signal
z = randperm(n);
x_initial(z(1:s)) = sign(randn(s,1));
figure;
subplot(3,1,1);
plot(1:n, x_initial); title('Original signal'); axis([0 512 -1 1])

A = randn(v,512);
A = A/max(max(abs(A)));
b = A*x_initial + 0.005 * randn(v,1);

% Compressed signal
subplot(3,1,2);
plot(1:v,b);
title("Compressed signal");
axis([0 v -1 1]);

% Reconstructed signal
x_recon = l1eq_pd(x_initial,A,[],b);
subplot(3,1,3);
plot(1:n,x_recon);
title("Reconstructed signal");
axis([0 n -1 1]);

% Correlation factor
corr = corrcoef(x_initial,x_recon)