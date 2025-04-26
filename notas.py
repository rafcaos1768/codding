{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNliHmQiBm8Z77CqrR6DUua"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RwrcCTWxJZ-w",
        "outputId": "317d3a45-2ff6-46ae-a576-efc88753a74e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "digite suas notas 5\n",
            "digite suas notas 4\n",
            "digite suas notas 6\n",
            "voce perdeu\n",
            "sua média é  5.0\n"
          ]
        }
      ],
      "source": [
        "#declaration\n",
        "note=0\n",
        "\n",
        "#begin_code\n",
        "\n",
        "for i in range(3):\n",
        "  note=int(input(\"digite suas notas \"))+note\n",
        "\n",
        "result=note/3\n",
        "\n",
        "if result >= 7:\n",
        "  print(\"voce passou\")\n",
        "  print(\"sua média é \",result)\n",
        "else:\n",
        "  print(\"voce perdeu\")\n",
        "  print(\"sua média é \",result)\n",
        "\n",
        "#end_code\n"
      ]
    }
  ]
}