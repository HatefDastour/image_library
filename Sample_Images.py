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
             'Rabbits', 'Squirrel', 'Varenna', 'Waterfront']

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
            'Lake_Como': 'A lake in Northern Italy’s Lombardy region.',
            'Northwest_Gate': 'Captures the Northwest Gate of Chongqing, China.',
            'Qiansimen_Bridge': 'Features the Qiansimen Bridge in Chongqing, China.',
            'Lunenburg': 'Lunenburg is a port town on the South Shore of Nova Scotia, Canada',
            'Rabbits': 'Depicts rabbits at Jericho Beach Park in Vancouver, BC, Canada.',
            'Squirrel': 'Features a squirrel at Sea to Sky Gondola in Vancouver, BC, Canada.',
            'Varenna': 'Portrays the picturesque village of Varenna on the shores of Lake Como, Italy.',
            'Waterfront': 'This image was taken from Vancouver Waterfront.'
        }

        if name not in self.Names:
            raise ValueError(f'Image name must be one of {
                             ", ".join(self.Names)}')

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
            raise ValueError(f'Image name must be one of {
                             ", ".join(self.Names)}')

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
        url = f'https://raw.githubusercontent.com/HatefDastour/image-library/main/images/{
            name}.jpg'
        return io.imread(url)