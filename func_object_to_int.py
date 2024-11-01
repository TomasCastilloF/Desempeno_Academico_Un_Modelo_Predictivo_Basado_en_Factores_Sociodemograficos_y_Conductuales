{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMXBMGhxX619HbT+DGUctAH",
      "include_colab_link": True
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TomasCastilloF/Desempeno-Academico-Un-Modelo-Predictivo-Basado-en-Factores-Sociodemograficos-y-Conductuales/blob/main/func_object_to_int.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "FpVLnb2l7GJS"
      },
      "outputs": [],
      "source": [
        "def convert_object_columns_to_int(df):\n",
        "    for col in df.select_dtypes(include=['object']).columns:\n",
        "        # Intentar convertir la columna a numérica\n",
        "        temp_series = pd.to_numeric(df[col], errors='coerce')\n",
        "\n",
        "        # Verificar si la columna tiene valores numéricos (sin NaN)\n",
        "        if temp_series.notna().all():\n",
        "            df[col] = temp_series.astype(int)  # Convertir a int\n",
        "\n",
        "    return df"
      ]
    }
  ]
}
