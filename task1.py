{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "LVFNix7RO2TA",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "2cb8a3ca-1c9d-4a34-aaec-74bc96b0974f"
      },
      "source": [
        "def is_triangle(a,b,c):\n",
        "    if(a > (b+c)):\n",
        "        print(\"No\")\n",
        "    elif(b > (a+c)):\n",
        "        print(\"No\")\n",
        "    elif(c > (a+b)):\n",
        "        print(\"No\")\n",
        "    else:\n",
        "        print(\"Yes\")\n",
        "\n",
        "a = int(input(\"Enter a side of triangle \"))\n",
        "b = int(input(\"Enter a side of triangle \"))\n",
        "c = int(input(\"Enter a side of triangle \"))\n",
        "\n",
        "is_triangle(a,b,c)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter a side of triangle 5\n",
            "Enter a side of triangle 55\n",
            "Enter a side of triangle 55\n",
            "Yes\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ATW-IbB4PHAa",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "6b566c38-183f-4521-9e9e-66bc19207884"
      },
      "source": [
        "word = \"Anish\"\n",
        "\n",
        "def first(word):\n",
        "    print( word[0])\n",
        "\n",
        "def last(word):\n",
        "    print( word[-1])\n",
        "    \n",
        "def middle(word):\n",
        "  print( word[1:-1])\n",
        "\n",
        "\n",
        "first(word)\n",
        "last(word)\n",
        "middle(word)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "A\n",
            "h\n",
            "nis\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fKWDpZ9SPV_L",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 346
        },
        "outputId": "973209f2-ba35-4736-8276-2f696d8b9b59"
      },
      "source": [
        "word = \"\"\n",
        "\n",
        "def first(word):\n",
        "    print( word[0])\n",
        "\n",
        "def last(word):\n",
        "    print( word[-1])\n",
        "    \n",
        "def middle(word):\n",
        "  print( word[1:-1])\n",
        "\n",
        "\n",
        "first(word)\n",
        "last(word)\n",
        "middle(word)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndexError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-8ad514ba3c02>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 13\u001b[0;31m \u001b[0mfirst\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     14\u001b[0m \u001b[0mlast\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     15\u001b[0m \u001b[0mmiddle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m<ipython-input-3-8ad514ba3c02>\u001b[0m in \u001b[0;36mfirst\u001b[0;34m(word)\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfirst\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m \u001b[0mword\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mlast\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mword\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mIndexError\u001b[0m: string index out of range"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IIpikTpdPYX6",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "\n",
        "def palindrome(word):\n",
        "\n",
        "    if word[0] == word[-1]:\n",
        "        if word[1] == word[-2]:\n",
        "            if word[2] == word[-3]:\n",
        "                print(\"it is a palindrome\")\n",
        "            else:\n",
        "                print(\"not a palindrome\")\n",
        "\n",
        "palindrome(\"Anish\")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xqjSYJAxQv_c",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}