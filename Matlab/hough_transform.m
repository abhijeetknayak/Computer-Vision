pkg load image;

function hough_image = hough_transform(img)
  
  img = imread('shapes.jpg');
  figure, imshow(img);

  gray_img = rgb2gray(img);
  figure, imshow(gray_img);

  edge_im = edge(gray_img, 'canny');
  figure, imshow(edge_im);

  s = size(edge_im, 1) + size(edge_im, 2); % Max number of rows in Transformed image

  H = zeros(s, 360); % Using theta as 360 degrees

  for i = 1:size(edge_im, 2)
    for j = 1:size(edge_im, 1)
      if edge_im(j, i) > 0 % Edge pixel
        for theta = 1:360
          d = (round(j*cos(theta) + i*sin(theta)));
          if d > 0
            H(d, theta) += 1; % Voting
          endif        
        endfor
      endif
    endfor
  endfor
  
  hough_image = H;  
endfunction



function [dfinal, thfinal, k] = extract_peaks(hough_image)
  

  k = 1;
  for i=1:size(hough_image, 1)
    for j=1:size(hough_image, 2)
      if hough_image(i, j) > 300
        dfinal(1, k) = i;
        thfinal(1, k) = j;
        k += 1;
      endif
    endfor
  endfor
endfunction




function line_image = find_lines(dfinal, thfinal, k, s)
  xvec = [1:1:s]';
  yf = zeros(s, k-1);
  yf = round((dfinal - xvec * cos(thfinal)) ./ sin(thfinal));
  fin = zeros(s, s);

  for i=1:s
    for j = 1:k-1
        if yf(i, j) > 0 && yf(i, j) <= s
          fin(i, yf(i, j)) = 255;
        endif    
    endfor
  endfor
  
  line_image = fin;
endfunction




image = imread('shapes.jpg');
hough_image = hough_transform(image);

dfinal = zeros(1, 500);
thfinal = zeros(1, 500);

[dfinal, thfinal, k] = extract_peaks(hough_image);

dfinal = dfinal(:, 1:k-1);
thfinal = thfinal(:, 1:k-1);

line_image = find_lines(dfinal, thfinal, k, size(image, 2));
figure, imshow(line_image);




