import Augmentor
p = Augmentor.Pipeline("data/farmer_market",output_directory="/work/augment-data")
# Add some operations to an existing pipeline.

# Add a horizontal flip operation to the pipeline:
p.flip_left_right(probability=0.4)

# Add a vertical flip operation to the pipeline:
p.flip_top_bottom(probability=0.8)

# Add a rotate90 operation to the pipeline:
p.rotate90(probability=0.1)
p.rotate(probability=0.7,max_left_rotation=10,max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)


#p.rotate270(probability=0.1)
#p.crop_random(probability=1, percentage_area=0.5)
#p.resize(probability=1.0, width=120, height=120)
#p.zoom_random(probability=0.5, percentage_area=0.8)
#p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)

p.sample(1000)
