rail_plot make-plot-groups-for-project --output_yaml ~/pz/projects/roman_7band_rubin/plots/pz_plots.yaml --plotter_yaml_path rail_project_config/plotting/pz_plots.yaml --split_mode by_flavor rail_project_config/roman/roman_7band_rubin.yaml 
rail_plot run --save_plots --purge_plots --make_html --outdir ~/pz/projects/roman_7band_rubin/plots ~/pz/projects/roman_7band_rubin/plots/pz_plots.yaml
cp -r ~/pz/projects/roman_7band_rubin/plots ~/public_html/roman_pz/plots/roman_7band_rubin 
