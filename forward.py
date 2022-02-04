# Basile Van Hoorick, Jan 2020
'''
Hallucinates beyond all four edges of an image, increasing both dimensions by 50%.
The outpainting process interally converts 128x128 to 192x192, after which the generated output is upscaled.
Then, the original input is blended onto the result for optimal fidelity.
Example usage:
python forward.py input.jpg output.jpg
'''
import matplotlib.pyplot as plt
from outpainting.basile.basile import perform_outpaint, load_model
from iop_utils import show_image
import os


def basile_outpaint(source, model, debug):
    op_frames = []
    for frame in source:
        output, blended = perform_outpaint(model, frame)
        if debug: show_image(blended)
        op_frames.append(blended)
    return op_frames


if __name__ == '__main__':
    src_file = os.path.join(os.getcwd(), 'test.png')
    for model in ['G_art.pt', 'G_nat.pt', 'G_rec.pt']:
        dst_file = os.path.join(os.getcwd(), model + '_output.png')
        model_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'models', 'basile', model)
        gen_model = load_model(model_path)
        print('Source file: ' + src_file + '...')
        input_img = plt.imread(src_file)[:, :, :3]
        output_img, blended_img = perform_outpaint(gen_model, input_img)
        plt.imsave(dst_file, blended_img)
        print('Destination file: ' + dst_file + ' written')
