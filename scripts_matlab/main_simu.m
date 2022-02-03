%---------------------------------------------------------------
% Simulations
% inputs:
%   - DEB parameters from allstat.m
%   - list of selected species and initial sizes
%   - temp .csv file
%   - array of food availabilities (fArr)
%
% calls: energy_budget.m
%
% created: 10/05/2021 - Ines Haberle
% modified: 26/09/2021 - Ines (za GIS kolegij)
% modified: 27/01/2022 - Ines (za HACKATHON)
%---------------------------------------------------------------
clear all
global aux
load('allstat');      % load all DEB parameters for all species
species_names = {'Sparus_aurata', 'Dicentrarchus_labrax', 'Scophthalmus_maximus'};  % define species of interest
initial_sizes = [5 5 5];  % define initial length each of farmed fished
file_names = {'Temp_Vrgada.csv', 'Temp_Ston.csv'};         % temperature files 

% Define array of food availabilities
fArr = [0.5:0.25:1]; 

for i = 1:length(file_names)
  for j = 1:length(species_names)
    Envfname = file_names{i};
    tT = readtable(Envfname);
    aux.tT = [tT{:,[1, 3]}]; % use temp from spreadsheet
    % aux.T = 20;            % use constant temp
      
    for k = 1:length(fArr)  % to run for all f's, kept constant during simulation
        species = species_names{j};
        aux.f = fArr(k);     % str = sprintf('%.2f',aux.f);
        aux.tArr = aux.tT(:,1);          % SIMULATION LENGTH
        aux.init_L = initial_sizes(j);   % Initial size (cm)

        % Load all metadata and parameters for given species
        p = allStat.(species); 

        % Initial conditions [E,V,H,R]; E - set to Emax/2, V - set to initial length, H - set to H according to current length scaled with Lp
        aux.IC = [(p.E_m*(aux.init_L*p.del_M)^3)/2, (aux.init_L*p.del_M)^3, min(p.E_Hp, p.E_Hp*((aux.init_L*p.del_M)/p.L_p)), 0];  

        %% Run simulation
        simu_KDEB.(strcat('f_',replace(num2str(aux.f),{'.'},{'_'}))) = feval('energy_budget',(1:max(aux.tArr))',p);        
    end
    
    %% Plot graphs
    % Initialize figures
    figL(j) = figure('Name', strcat(species_names{j},'_Length_',erase(file_names{i},{'Temp_','.csv'}))); %,'_f',num2str(aux.f)));
     title('Length');    %(strcat('Length @ f = ', num2str(aux.f)));
     xlabel('date, d');
     ylabel('length, cm');
     yyaxis right;
     plot(tT.date,tT.sst-273.15,'b:'); % plot temperature
     ylabel('temp, °C'); ylim([10 30]);
    figW(j) = figure('Name', strcat(species_names{j},'_Weight_',erase(file_names{i},{'Temp_','.csv'}))); %,'_f',num2str(aux.f)));
     title('Weight');    %(strcat('Weight @ f = ', num2str(aux.f)));
     xlabel('date, d');
     ylabel('weight, g'); 
     yyaxis right;
     plot(tT.date,tT.sst-273.15,'b:','DisplayName', 'temp');  % plot temperature
     ylabel('temp, °C'); ylim([10 30]);
    
    fdnames = fieldnames(simu_KDEB);
    cmp = colormap(lines);
    for k = 1 : length(fdnames)
     str = num2str(fArr(k));
     % Length
      set(0, 'CurrentFigure', figL(j))
      yyaxis left; hold on
      plot(tT.date(1:end-1), simu_KDEB.(fdnames{k})(:,2), 'DatetimeTickFormat', 'MM/yyyy', 'DisplayName', str, 'LineStyle', '-', 'Color', cmp(k,:)); %,'r-'
      ylim auto;
      

      % Weight
      set(0, 'CurrentFigure', figW(j))
      yyaxis left; hold on
      plot(tT.date(1:end-1), simu_KDEB.(fdnames{k})(:,3), 'DatetimeTickFormat', 'MM/yyyy', 'DisplayName', str, 'LineStyle', '-', 'Color', cmp(k,:)); % ,'r-'
      ylim auto;
     
    end
    % Save figures
    saveas(figL(j), strcat(figL(j).Name,'.png'));
    saveas(figW(j), strcat(figW(j).Name,'.png'));
  end
end