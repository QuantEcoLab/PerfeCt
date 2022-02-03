function output = dydt_KDEB(t, EVHR, p)
global aux

%% Unpack state vars
E  = EVHR(1); % J, reserve energy
V  = EVHR(2); % cm^3, structural volume
E_H  = EVHR(3); % J , cumulated energy inversted into maturity 
E_R  = EVHR(4); % J, reproduction buffer

vars_pull(p);

%% Metamorphosis check (set acceleration factor)
 if E_H <= E_Hb
    s_M = 1; % acceleration factor before and at birth;
 elseif E_H > E_Hb && E_H < E_Hj
    s_M = V^(1/3)/L_b; % acceleration factor between birth and metamorposis;
 end

%% Temperature correction function (details in Kooijman 2010, p. 21)
%  
 if ismember('tT',fieldnames(aux))
    T = spline1(t, aux.tT);      % use when have temperature vector in time
 else
    T = aux.T + 273.15;
 end

 if ismember('tf',fieldnames(aux))
    f = spline1(t, aux.tf);       % use when have feeding vector in time
 else
    f = aux.f;
 end
 c_T = exp(T_A/ T_ref - T_A/ T);

 p_AmT = c_T * p_Am * s_M;
 v_T = c_T * v * s_M;
 p_MT = c_T * p_M;
 p_TT = c_T * p_T;
 k_JT = c_T * k_J; 
 p_XmT = p_AmT / kap_X;

%% Energy fluxes

% Feeding
 if E_H < E_Hb
    pX = 0; % embryo stage -> f=0
 else
    pX = f * p_XmT * V^(2/3);
 end

% Fluxes
 pA = kap_X * pX;
 pM = p_MT * V;
 pT = p_TT * V^(2/3);
 pS = pM + pT;
 pC = (E/V) * (E_G * v_T * V^(2/3) + pS ) / (kap * E/V + E_G); %eq. 2.12 p.37 Kooijman 2010
 pJ = k_JT * E_H;

% Energy amount check - is there enough in the reseve for maintenance?
 if pA < (kap * pC) && (kap * pC) < pS && E < pS
    output = [-E; 0; 0; 0];
    return
 end
 
%% Differential equations for state variables
 dE = pA - pC;  % dE/dt
 dV = max (0, (kap * pC - pS) / E_G); % dV/dt, max function does not allow shrinking (remove if you want to deplete structure)
 if E_H < E_Hp
    dH = max (0, (1 - kap) * pC - pJ); % dEH/dt
    dR = 0; % dER/dt
 else
    dH = 0;
    dR = max (0, (1 - kap) * pC - pJ); % dR/dt, max function does not allow shrinking of repro buffer (remove if you want to deplete repro buffer)
 end
 
output = [dE; dV; dH; dR];

end