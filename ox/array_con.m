%

function [ val] = array_con(m, n)
  a = ones(m, n); 
  for i = 1:m
    for j = 1:n
      a(i, j) = i + j - 1; 
    endfor 
  endfor 
  val = a; 

  end

