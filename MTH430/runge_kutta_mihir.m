%% Example usage
lat0 = 0;  % latitude in degrees
lon0 = 0;  % longitude in degrees
v0 = 6000;  % speed in m/s
gam0 = 0;  % flight path angle in degrees
phi0 = pi/9;  % azimuth angle in radians
h = 0.2;  % time step in seconds
T = 890;  % final time in seconds

[Px, Py, Pz] = EOM_RK4(lat0, lon0, v0, deg2rad(gam0), phi0, h, T);
fprintf('Final Point = (%.4g, %.4g, %.4g)\n', Px(end), Py(end),Pz(end));

function [Px, Py, Pz] = EOM_RK4(lat0, lon0, v0, gam0, phi0, h, T)

    %% Number of steps
    nSteps = floor(T/h);
    h0 = T/nSteps;  % Adjusted time step to ensure T/h0 = N is an integer

    %% Space allocations
    P = zeros(3, nSteps+1);
    V = zeros(3, nSteps+1);

    %% Parameters
    r0 = 6378137;  % Earth's radius in meters
    mu = 3986004.418e8;  % Gravitational constant times Earth's mass
    J2 = 1091.3e-6;  % Second zonal harmonic

    % Gravity function
    G = @(r, Qx, Qy, Qz) ...
        [-mu*Qx*((r0/r)^2 + 3*J2*(r0/r)^4*(1 - 5*(Qz/r)^2)/2)/(r0^2*r);...
         -mu*Qy*((r0/r)^2 + 3*J2*(r0/r)^4*(1 - 5*(Qz/r)^2)/2)/(r0^2*r);...
         -mu*Qz*((r0/r)^2 + 3*J2*(r0/r)^4*(3 - 5*(Qz/r)^2)/2)/(r0^2*r)];

    %% Initial conditions
    lat0 = deg2rad(lat0);
    lon0 = deg2rad(lon0);
    
    % Initial position in ECI coordinates
    P(:,1) = [r0*cos(lat0)*cos(lon0); r0*cos(lat0)*sin(lon0); r0*sin(lat0)];
    
    % Velocity transformation matrix
    M = [-sin(lat0)*cos(lon0), -sin(lat0)*sin(lon0), cos(lat0);...
         -sin(lon0), cos(lon0), 0;...
         cos(lat0)*cos(lon0), cos(lat0)*sin(lon0), sin(lat0)];
     
    V(:,1) = M * [v0*cos(gam0)*cos(phi0); v0*cos(gam0)*sin(phi0); v0*sin(gam0)];
    
    %% RK4 Integration
    for i = 1:nSteps
        % Current state
        r = norm(P(:,i));
        
        % k1
        k1P = V(:,i);
        k1V = G(r, P(1,i), P(2,i), P(3,i));
        
        % k2
        k2P = V(:,i) + 0.5*h0*k1V;
        k2V = G(norm(P(:,i) + 0.5*h0*k1P), ...
                P(1,i) + 0.5*h0*k1P(1), ...
                P(2,i) + 0.5*h0*k1P(2), ...
                P(3,i) + 0.5*h0*k1P(3));
        
        % k3
        k3P = V(:,i) + 0.5*h0*k2V;
        k3V = G(norm(P(:,i) + 0.5*h0*k2P), ...
                P(1,i) + 0.5*h0*k2P(1), ...
                P(2,i) + 0.5*h0*k2P(2), ...
                P(3,i) + 0.5*h0*k2P(3));
        
        % k4
        k4P = V(:,i) + h0*k3V;
        k4V = G(norm(P(:,i) + h0*k3P), ...
                P(1,i) + h0*k3P(1), ...
                P(2,i) + h0*k3P(2), ...
                P(3,i) + h0*k3P(3));
        
        % Update position and velocity
        P(:,i+1) = P(:,i) + (h0/6)*(k1P + 2*k2P + 2*k3P + k4P);
        V(:,i+1) = V(:,i) + (h0/6)*(k1V + 2*k2V + 2*k3V + k4V);
    end

    % Extracting outputs
    Px = P(1,:);
    Py = P(2,:);
    Pz = P(3,:);

end