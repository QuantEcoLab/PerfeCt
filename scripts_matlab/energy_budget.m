function rez = energy_budget(tArr, p)
 %---------------------------------------------------------------
 % Compute model predictions (numerical integration)
 %  
 % tArr: time points to be used to make simulations
 % p: structure with individual features (parameters, env...),; see init.m
 % 
 % DEB
 %    tEVHR - matrix with time and state variables
 %    t , d, time
 %    E , J, reserve energy
 %    V , cm^3, structural volume
 %    E_H , J , cumulated energy inversted into maturity
 %
 % called by : main_simu.m
 % calls : dydt_KDEB.m
 %
 % created: 01/04/2021; modified 30/04/2021 - Ines Haberle
 % modified: 27/01/2022 - Ines Haberle
 %---------------------------------------------------------------

global aux

i = 0; % initialize year index
IC = aux.IC;
% tArr = fitData(2:end,1);
% tArr = data(~isnan(data(:,1)));
tmax = max(tArr); % simulation time
tc = tArr(1); % set current time to initial time
rezTmp = []; % initialize outputs
while tc < tmax        % while loop is used to loop for each year and account for reproduction each year
      i = i + 1;       % spawning every year
      tnext = 365*i;   % integrate two spawning dates (one spawning each year)
      if tnext > tmax
        tnext  = tmax;
      end
      t = tArr(tArr >= tc & tArr <= tnext,1); % select times for each year (1-365, 365-730, etc.)
      disp(t)
      options = odeset; % (options, 'Events', @Ezero); % add an events
      [time, EVHR] = ode45(@dydt_KDEB, t, IC, options, p);  % RUN DIFFERENTIAL EQUATION SOLVER TO CALCULATE STATE VARIABLES
      rezTmp = [rezTmp; [time,EVHR]];  % append to output
      E_Hc = EVHR(end,3);
      if E_Hc >= p.E_Hp
        EVHR(end,4) = 0;
      end
      IC = EVHR(end, :)';
      tc = time(end)+1;
end
 L = rezTmp(:,3).^(1/3)./p.del_M;        % calculate physical length from structural
 W = rezTmp(:,3) * (1 + aux.f * p.ome);  % W = V * (1+ f*ohm) % calculate weight
 rez = [ rezTmp(:,1) L W];

end

%% Event function to terminate at E < pS // Locates the time when reserve is not enough for maintenance
function [value,isterminal,direction] = Ezero(t,EVHR,p)
    check = EVHR(1)>0;
    value = check;  % detect values at zero, terminates when this value is 0, i.e when E>0 is not true.
    isterminal = 1; % stop the integration 
    direction = 0;
end
