# Build all the pipelines
rail_project build --flavor all --force rail_project_config/roman/roman_3band_rubin.yaml 

# These will run the photometric errors pipeline and make the test / train data sets
rail_project run phot-errors --flavor baseline --selection roman_wl rail_project_config/roman/roman_3band_rubin.yaml 
rail_project subsample --catalog_template degraded --subsampler_class_name random_subsampler --selection roman_wl --flavor baseline --basename output_dereddener_errors.pq --file_template test_file_100k --subsample_name test_100k rail_project_config/roman/roman_3band_rubin.yaml 
rail_project subsample --catalog_template degraded --subsampler_class_name random_subsampler --selection roman_wl --flavor baseline --basename output_dereddener_errors.pq --file_template train_file_100k --subsample_name train_100k rail_project_config/roman/roman_3band_rubin.yaml 

# Hack to get rid of np.inf
python inf_to_nan_roman.py

# Run the pz pipeline
rail_project run pz --flavor baseline --selection roman_wl rail_project_config/roman/roman_3band_rubin.yaml 
