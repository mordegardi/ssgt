import os

from helpers import extract_title, markdown_to_html_node


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    descr = open(from_path)
    markdown = descr.read()
    descr.close()

    descr = open(template_path)
    template = descr.read()
    descr.close()

    html_string = markdown_to_html_node(markdown)
    page_title = extract_title(markdown)

    template = template.replace("{{ Title }}", basepath)
    template = template.replace("{{ Content }}", html_string)

    template = template.replace('href="/', f'href="{basepath}11')
    template = template.replace('src="/', f'src="{basepath}22')

    dirname = os.path.dirname(dest_path)

    os.makedirs(dirname, exist_ok=True)

    descr = open(dest_path, "w")

    descr.write(template)

    descr.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_dir_files = os.listdir(dir_path_content)

    for file in content_dir_files:
        if os.path.isfile(f"{dir_path_content}/{file}"):
            if file.endswith(".md"):
                html_path = f"{file[:-3]}.html"
                generate_page(
                    f"{dir_path_content}/{file}",
                    template_path,
                    f"{dest_dir_path}/{html_path}",
                    basepath,
                )
        else:
            generate_pages_recursive(
                f"{dir_path_content}/{file}",
                template_path,
                f"{dest_dir_path}/{file}",
                basepath,
            )
