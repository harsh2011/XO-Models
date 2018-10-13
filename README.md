# XO-Models
Code of models trained while creating XO application. CNN model to differ X and O that are drawn by user in 28 x 28 canvas. GAN use to draw from the computer side

## Dataset Samples
![Image](Dataset/SampleO/0_0_1.png)
![Image](Dataset/SampleX/__0_2.png)

## Generated Samples from GANs
![Image](gen_o.PNG)
![Image](gen_x.PNG)

## App Results
![](AppDemowithGAN.gif)

## Frozen graph of CNN
at out/opt_xo_differ.pb <br />
	input_node_name = 'input' <br />
	keep_prob_node_name = 'keep_prob' <br />
	output_node_name = 'output' <br />

## Frozen graph of GAN_O
at GAN_O/opt_gan_O.pb <br />
	input_node_name = 'noise_input_o' <br />
	output_node_name = 'gen_o' <br />

## Frozen graph of GAN_X
at GAN_X/opt_gan_X.pb <br />
	input_node_name = 'noise_input_x' <br />
	output_node_name = 'gen_x' <br />