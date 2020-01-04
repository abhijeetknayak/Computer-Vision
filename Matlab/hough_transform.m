##pkg load image;
##
##img = imread('shapes.jpg');
####figure, imshow(img);
##
##gray_img = rgb2gray(img);
####figure, imshow(gray_img);
##
##edge_im = edge(gray_img, 'canny');
####figure, imshow(edge_im);
##
##s = size(edge_im, 1) + size(edge_im, 2);
##
##H = zeros(s, 360);
##
##for i = 1:size(edge_im, 2)
##  for j = 1:size(edge_im, 1)
##    if edge_im(j, i) > 0
##      for theta = 1:360
##        d = (round(j*cos(theta) + i*sin(theta)));
##        if d > 0
##          H(d, theta) += 1;
##        endif        
##      endfor
##    endif
##  endfor
##endfor
##
##disp('Reached');
##figure, imshow(H, []);

dfinal = zeros(1, 500);
thfinal = zeros(1, 500);
k = 1;
for i=1:size(H, 1)
  for j=1:size(H, 2)
    if H(i, j) > 300
      dfinal(1, k) = i;
      thfinal(1, k) = j;
      k += 1;
    endif
  endfor
endfor

dfinal = dfinal(:, 1:k-1);
thfinal = thfinal(:, 1:k-1);

xvec = [1:1:1200]';
yf = zeros(1200, k-1);
yf = round((dfinal - xvec * cos(thfinal)) ./ sin(thfinal));
fin = zeros(1200, 1200);

for i=1:1200
  for j = 1:k-1
      if yf(i, j) > 0 && yf(i, j) <= 1200
        fin(i, yf(i, j)) = 255;
      endif    
  endfor
endfor

fin = fin .* edge_im;
figure, imshow(fin);




