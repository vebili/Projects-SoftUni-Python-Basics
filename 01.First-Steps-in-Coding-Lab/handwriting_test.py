import pywhatkit

encoding = 'utf-8'
pywhatkit.text_to_handwriting(
    'To use this data in your Python code you must give a valid utf-8 encoding '
    'declaration at the top of the script, and you also must tell your text editor '
    'to save the file with the utf-8 encoding.'
    'Маратонките са изработени от висококачествени материали, от които ще останете очаровани. '
    'Новите разработки на маратонки и кецове са вдъхновени от последните модни тенденции в Европа и света. '
    'С тях получавате удобството, което винаги сте търсили. '
    'Runners дава гаранция за качество на всеки един от своите продукти.', rgb=(0, 0, 255)
)