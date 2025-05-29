from textnode import TextNode, TextType

def main():
    node = TextNode("This is a TextNode", TextType.LINK, "https://www.boot.dev")
    print(node)

main()