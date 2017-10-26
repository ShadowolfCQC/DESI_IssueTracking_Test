#! /usr/bin/python

import numpy
from astropy.table import Table
from matplotlib import rcParams
from matplotlib import pyplot
from photutils.datasets import make_gaussian_sources
from photutils.datasets import make_noise_image
import random

#Create random values for placement of star, star size, and background noise intensity
size=(random.randint(2.,7.))
placex=(random.randint(5,45))
placey=(random.randint(5,45))
amp=(random.randint(25,150))

#Created data table for size and position of Gaussian simulation
sigma_psf = 2.0
sources = Table()
sources['amplitude'] = [amp] #controls intensity of background noise
sources['x_mean'] = [placex] #controls position of star
sources['y_mean'] = [placey]
sources['x_stddev'] = [size] #controls size and shape of star
sources['y_stddev'] = [size]
sources['theta'] = numpy.array([0]) * numpy.pi / 180.
tshape = (50, 50)


#build Gaussian image and back ground noise
image1 = make_gaussian_sources(tshape, sources)
image2 = image1 + make_noise_image(tshape, type='gaussian', mean=0., stddev=2., random_state=1)

rcParams['font.size'] = 13


#Create figure to place images in
fig, axs = pyplot.subplots(nrows=1, ncols=2,)
ax = axs[0]
ax.imshow(image2, cmap='viridis', aspect=1, interpolation='nearest',
	origin='lower') #affects coloring of image
ax.set_title('With Background Noise')
ax = axs[1]
ax.imshow(image1, cmap='viridis', aspect=1, interpolation='nearest',
	origin='lower') #affects coloring of image
ax.set_title('No Background Noise')
pyplot.show()
