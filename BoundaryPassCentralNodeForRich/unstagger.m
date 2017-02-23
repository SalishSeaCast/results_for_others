function [ u, v] = unstagger(ugrid, vgrid)
    u1 = (ugrid(:, 1:end-1) + ugrid(:, 2:end)) * 0.5;
    v1 = (vgrid(1:end-1, :) + vgrid(2:end, :)) * 0.5;
    u = u1(2:end, :);
    v = v1(:, 2:end);