import click
import logging
import locale


from asvp.classes.pointisotherm import PointIsotherm
from asvp.classes.adsorbate import Adsorbate


logger = logging.getLogger(__name__)

@click.command()
@click.option('--siteurl', default="http://anfitria.club", help='Site to scrap')
@click.option('--sfile', default="scrap2.html", help='Storage File')
def siteload (sfile, siteurl):

    locale.setlocale(locale.LC_ALL, '')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(msecs).2f - %(levelno)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logger.info('Starting asvp server...')

    with open(r'../data/carbon_x1_n2.json') as f:
        isotherm = PointIsotherm.from_json(f.read())

    isotherm.print_info(False)





if __name__ == '__main__':
    siteload()






    # my_adsorbate = Adsorbate(
    #     'butane',  # Required
    #     formula='C4H10',  # Recognised
    #     #         alias = [n-butane, Butane],        # Recognised
    #     backend_name='butane',  # Recognised, Required for CoolProp interaction
    #     saturation_pressure=2.2,  # Recognised
    #     carbon_number=4,  # User specific
    # )
    #
    # print(my_adsorbate)
    #
    # p = my_adsorbate.saturation_pressure(298, unit='mmHg')
    #
    # print (p)
    #
    # isotherm = PointIsotherm(
    #     pressure=[0.1, 0.2, 0.3, 0.4, 0.5, 0.45, 0.35, 0.25, 0.15, 0.05],
    #     loading=[0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.15, 0.05],
    #     material_name='Carbon',
    #     material_batch='X1',
    #     adsorbate='N2',
    #     t_iso=77,
    # )
    #
    # print (isotherm)
