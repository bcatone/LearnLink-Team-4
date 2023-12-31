���      }�(�recommend_setting��
dill._dill��_create_function���(h�_create_code���(KK K KKKCTt ���t�fdd�|D �d�}|s(dS |�dg �}|s<dS t|� fdd�d�}|S �(X�  
    Recommend the setting type for a given disability_id based on the highest coefficient.

    Parameters:
    - disability_id (int): The disability_id for which to recommend the setting.
    - disability_settings (list): List of dictionaries containing disability settings.
    - coefficients_dict (dict): Dictionary mapping setting types to their coefficients.

    Returns:
    - dict: The dictionary associated with the recommended_setting.
    �h(KK K KKK3C| ]}|d  � kr|V  qdS ��disability_id�N��)�.0��entry����<ipython-input-79-edb53c1eca36>��	<genexpr>�KC   �h
��)t�R��$recommend_setting.<locals>.<genexpr>�N�accessibility_types�h(KK K KKKC� � | d d�S �N�setting_type�K ���get���h��h�<lambda>�KC ��coefficients_dict���)t�R��#recommend_setting.<locals>.<lambda>��key���t�(�int��next�h�max�t�(h
�disability_settings�h�disability_entry��relevant_setting_types��recommended_setting_type�t�hhKC �)hh
��t�R�c__builtin__
__main__
h]�(}�(h
J�J]h]�(}�(h�	90000001A��
font_color��charcoal��background_color��pastel light blue��	font_size�K�font_weight��regular��font_family��	Trebuchet��letter_spacing�G@      �line_spacing�G@6�     �word_spacing�G@S�     �text_alignment��left aligned��is_auto_play_tts���bionic_reading���lists_with_bullets���wcag_compliant���	score_avg�KU�	score_std�Ku}�(h�	90000001B�h9�licorice�h;�pastel light yellow�h=Kh>h?h@�Tahoma�hBG@������hCKhDG@R`     hEhFhG�hH�hI�hJ�hKKPhLKu}�(h�	90000001C�h9�onyx�h;�light cream�h=Kh>h?h@�Century Gothic�hBG@������hCKhDK?hEhFhG�hH�hI�hJ�hKK_hLKu}�(h�	90000001D�h9�matte black�h;�
light gray�h=Kh>h?h@�	Open Sans�hBG@333333hCG@3�     hDG@Q     hEhFhG�hH�hI�hJ�hKK_hLKu}�(h�	90000001E�h9�white�h;�red�h=Kh>h?h@h[hBG@ffffffhCG@      hDG@>@     hEhFhG�hH�hI�hJ�hKK7hLK-ueu}�(h
J�J]h]�(}�(h�	90000002A�h9�	dark gray�h;�eggshell�h=Kh>h?h@h[hBG?��Q��hCKhDG@z�G�{hEhFhG�hH�hI�hJ�hKK_hLKu}�(h�	90000002B�h9�midnight blue�h;�ivory�h=Kh>h?h@�Lexend�hBG?�
=p��
hCKhDG?��Q��hEhFhG�hH�hI�hJ�hKK_hLKu}�(h�	90000002C�h9h:h;hZh=Kh>h?h@�	Helvetica�hBG?��G�z�hCG@8�     hDG@��Q�hEhFhG�hH�hI�hJ�hKKZhLKu}�(h�	90000002D�h9�yellow�h;�orange�h=K	h>h?h@hmhBG?��G�z�hCG@)      hDG?��
=p��hEhFhG�hH�hI�hJ�hKK2hLK7ueu}�(h
J�J]h]�(}�(h�	90000003A�h9�
nightrider�h;�quartz�h=Kh>�bold�h@�Poppins�hBG?�������hCG@6�     hDG@333333hEhFhG�hH�hI�hJ�hKK_hLKu}�(h�	90000003B�h9�black russian�h;�prim�h=Kh>h?h@�Source Sans Pro�hBG@G�z�HhCKhDG@
=p��
hEhFhG�hH�hI�hJ�hKKZhLKu}�(h�	90000003C�h9h:h;�linen�h=Kh>h?h@hVhBG@
=p��
hCK$hDG@�Q��hEhFhG�hH�hI�hJ�hKKUhLKu}�(h�	90000003D�h9�green�h;hph=K
h>h?h@hVhBG?�z�G�hCKhDG?�p��
=qhEhFhG�hH�hI�hJ�hKK7hLK-ueue}�(h8K �	90000001B��numpy.core.multiarray��scalar����numpy��dtype����f8�����R�(K�<�NNNJ����J����K t�bCD2�g�����R��	90000001C�h�h�C�u*=@���R��	90000001D�h�h�C��I@���R��	90000001E�h�h�C��0�>����R��	90000002A�h�h�C��ֽ!�@���R��	90000002B�h�h�C����ۂ@���R��	90000002C�h�h�C�F�gI�?���R��	90000002D�h�h�Cv[���@����R��	90000003A�h�h�C��@�G�?���R��	90000003B�h�h�C��+@=d @���R��	90000003C�h�h�Ce�v�L����R��	90000003D�h�h�C΀OV?����R�u��Nt�R�}�}�(�__doc__�h�__annotations__�}�u��bh+h4hh�u.