function [ueast, vnorth] = rotate_vel(u_in, v_in)
    theta_rad = 29 * pi / 180;
    
    ueast = u_in * cos(theta_rad) - v_in * sin(theta_rad);
    vnorth = u_in * sin(theta_rad) + v_in * cos(theta_rad);