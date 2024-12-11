from skimage import io

class Sample_Images:
    '''
    A class for providing descriptions and images of images.

    Attributes:
    Names (list): List of available image names.

    Methods:
    description(name):
    - Provides a description of the given image name.

    read_image(name):
    - Reads and returns the image as a matrix for the given image name.

    title(name):
    - Removes underscores from the image name and provides a formatted title.

    '''
    Names = ['Lake_Como', 'Northwest_Gate', 'Qiansimen_Bridge', 'Lunenburg',
             'Rabbits', 'Squirrel', 'Varenna', 'Waterfront',
             'Botanical_Garden', 'Calgary_Fall', 'Hong_Kong']

    def __init__(self):
        pass

    def description(self, name):
        '''
        Provides a description for the given image name.

        Parameters:
        name (str): The name of the image.

        Returns:
        description (str): A description of the image.
        '''
        descriptions = {
            'Lake_Como': 'A scenic lake located in Northern Italy’s Lombardy region, known for its picturesque surroundings and historic villages.',
            'Northwest_Gate': 'Captures the Northwest Gate of Chongqing, China, a significant landmark in the city’s rich cultural and historical landscape.',
            'Qiansimen_Bridge': 'Features the Qiansimen Bridge in Chongqing, China, a notable example of modern engineering and urban development.',
            'Lunenburg': 'Lunenburg is a charming port town on the South Shore of Nova Scotia, Canada, famous for its well-preserved 18th-century architecture and maritime history.',
            'Rabbits': 'Depicts a group of rabbits at Jericho Beach Park in Vancouver, BC, Canada, showcasing the park’s natural beauty and wildlife.',
            'Squirrel': 'Features a squirrel at Sea to Sky Gondola in Vancouver, BC, Canada, highlighting the area’s diverse wildlife and scenic views.',
            'Varenna': 'Portrays the picturesque village of Varenna on the shores of Lake Como, Italy, known for its colorful houses, narrow streets, and stunning lake views.',
            'Waterfront': 'This image was taken from Vancouver Waterfront, capturing the city’s vibrant urban landscape and scenic waterfront area.',
            'Botanical_Garden': 'An image of the Kunming Botanical Garden, showcasing the garden’s diverse plant species and serene natural environment.',
            'Calgary_Fall': 'An image from a neighborhood park in Calgary during the fall season, highlighting the city’s autumn colors and park scenery.',
            'Hong_Kong': 'Features Victoria Harbour in Hong Kong, a natural landform harbour separating Hong Kong Island from the Kowloon Peninsula, known for its stunning skyline, bustling port activities, and nightly light shows.'
        }

        if name not in self.Names:
            raise ValueError(f'Image name must be one of {", ".join(self.Names)}')

        return descriptions[name]

    def title(self, name):
        '''
        Removes underscores from the image name and provides a formatted title.

        Parameters:
        name (str): The name of the image.

        Returns:
        title (str): A formatted title for the image.
        '''
        if name not in self.Names:
            raise ValueError(f'Image name must be one of {", ".join(self.Names)}')

        return name.replace("_", " ")

    def read_image(self, name):
        '''
        Reads and returns the image as a matrix for the given image name.

        Parameters:
        name (str): The name of the image.

        Returns:
        image (ndarray): The loaded image in ndarray format.
        '''
        if name not in self.Names:
            raise ValueError(f'Image name must be one of {", ".join(self.Names)}')

        # Update the URL to point to your new GitHub repository
        url = f'https://raw.githubusercontent.com/HatefDastour/image_library/main/images/{name}.jpg'
        return io.imread(url)