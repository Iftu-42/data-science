{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNvfNkHhvug94lglSekhmP4",
      "include_colab_link": true
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
        "<a href=\"https://colab.research.google.com/github/Iftu-42/Iftu-42/blob/main/Untitled1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3CoiZOh_K5Y1"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. What is the difference between a list, a dictionary, and a NumPy array? Give one example of each.\n",
        "# All are used to store data but\n",
        "a,list is enclosed with square brace and its mutable this means data can change and we can enter any types of data in one list.\n"
      ],
      "metadata": {
        "id": "UqCu3MWaLqVj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list=[\"apple\",\"mango\",\"23\",\"3.78\"]\n",
        "print(list)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RVG6j86TNVrF",
        "outputId": "02082e4d-0a19-4b8f-d666-bcb379578aa8"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'mango', '23', '3.78']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "b,dictionary is enclosed in curly brace and it have what we call key and value which make it different from others and the key is immutable but the value is mutable.\n"
      ],
      "metadata": {
        "id": "a2No23mjNvLN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "dict={\"house\":\"villa\",\"car\":\"BMW\",\"NUMBER\":\"45677\"}\n",
        "print(dict[\"car\"])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DIGDqAbiOKXr",
        "outputId": "21862e7c-dd5a-453b-ff35-8e10b6e4b1b0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "BMW\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "c,Numpy array is alternative way to python list but calculation set for ach element within a numpy array and it only contain single data type.\n"
      ],
      "metadata": {
        "id": "_XhfASC3PRGT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "# grams of [protein, carbohydrate, fat]\n",
        "grams=[60,120,40]\n",
        "# calories per gram for [protein, carbohydrate, fat]\n",
        "calpgram=[5,7,8]\n",
        "grams=np.array(grams)\n",
        "import numpy as np\n",
        "# grams of [protein, carbohydrate, fat]\n",
        "grams=[60,120,40]\n",
        "# calories per gram for [protein, carbohydrate, fat]\n",
        "calpgram=[5,7,8]\n",
        "grams=np.array(grams)\n",
        "calpgram=np.array(calpgram)\n",
        "calpernut=grams*calpgram\n",
        "print(\"Calories per nutrient:\",calpernut)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ElSEhGt4RRE5",
        "outputId": "5cf07ead-6b78-4d9f-c38d-044d1eb77c0f"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Calories per nutrient: [300 840 320]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Given the list [10, 15, 20, 25, 30], write a function that returns the square of only even numbers.\n",
        "answer\n"
      ],
      "metadata": {
        "id": "THQ_4iuhYMCm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def SEN(list):\n",
        "  list=[10,15,20,25,30]\n",
        "  for i in list:\n",
        "    if i%2==0:\n",
        "      print(i**2)\n",
        "SEN(list)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mxNG8hZ5YTUP",
        "outputId": "8e46f8ee-1d30-4500-fe49-e114baf0f207"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "100\n",
            "400\n",
            "900\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. What does the following code output, and why?\n"
      ],
      "metadata": {
        "id": "5jWFj8DgYuHC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = [1, 2, 3]\n",
        "y = x\n",
        "y.append(4)\n",
        "print(x)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kDGAqSCwY6XA",
        "outputId": "9d6153bb-6391-4584-929e-a939440ea5df"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In Python, when you do y = x, both y and x point to the same list. So, if you change y (like y.append(4)), it will also change x.\n"
      ],
      "metadata": {
        "id": "tYk8jljwZbc9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "4. What does .shape and .describe() tell you about a pandas DataFrame? Show using an example.\n",
        "answer:\n",
        ".shape will tell you the dimension of dataframe means how many column and raws are there.\n",
        ".describe() will tell the dataframe summary things like mean,min,max and so on.\n",
        "I USE EXAMPLE THE ANSWER OF QUESTION NUMBER FIVE."
      ],
      "metadata": {
        "id": "dQhPUgO1ZwO8"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "5. Load this CSV: airtravel.csv\n",
        "Print the first 5 rows\n",
        "What do you notice about the data?\n"
      ],
      "metadata": {
        "id": "jcnSI9rmbVg0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "airtravel = {\n",
        "    'month': ['JAN','FEB', 'MARCH','APRIL'],\n",
        "    '1958': [340, 318,362,348],\n",
        "    '1959': [360,342,406,396],\n",
        "    '1960':[417,391,419,461]\n",
        "}\n",
        "\n",
        "AT = pd.DataFrame(airtravel)\n",
        "print(\"Shape of DataFrame:\", AT.shape)\n",
        "print(\"Statistical Summary of Numeric Columns:\")\n",
        "print(AT.describe())\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sZYY2qtSflZS",
        "outputId": "00df3065-8445-45ec-e342-0677c7864e46"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Shape of DataFrame: (4, 4)\n",
            "Statistical Summary of Numeric Columns:\n",
            "             1958        1959        1960\n",
            "count    4.000000    4.000000    4.000000\n",
            "mean   342.000000  376.000000  422.000000\n",
            "std     18.402898   30.066593   28.959742\n",
            "min    318.000000  342.000000  391.000000\n",
            "25%    334.500000  355.500000  410.500000\n",
            "50%    344.000000  378.000000  418.000000\n",
            "75%    351.500000  398.500000  429.500000\n",
            "max    362.000000  406.000000  461.000000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The first column is Month and The other columns are numbers showing how many people traveled by air each month for different years.\n"
      ],
      "metadata": {
        "id": "Dan8fLf6jQmK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "6.Load the CSV from Q5 and find:\n",
        "  The month with the highest total passengers\n",
        "  The month with the lowest in 1958\n",
        "  "
      ],
      "metadata": {
        "id": "TxfRm5Y-jlhz"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "7.  What does the .groupby() function do in pandas? Show an example using dummy data.\n",
        "It groups data by a specific column and then does something to each group, like adding up the numbers or finding the average.\n",
        "in this example it add up number of fruits."
      ],
      "metadata": {
        "id": "3gdJdsQUlbwl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "fruits = {\n",
        "    'Fruit': ['Apple', 'Banana', 'orange', 'Banana', 'orange'],\n",
        "    'Quantity': [5, 3, 7, 6, 2]\n",
        "}\n",
        "fr = pd.DataFrame(fruits)\n",
        "grouped = fr.groupby('Fruit').sum()\n",
        "print(grouped)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yaz_I-x9mXH9",
        "outputId": "fdbc2c36-3593-4ec6-8e8e-2bba5e02e6f2"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        Quantity\n",
            "Fruit           \n",
            "Apple          5\n",
            "Banana         9\n",
            "orange         9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. Load the Titanic dataset from seaborn and:\n",
        "\n",
        "  Count how many missing values are in each column  \n",
        "  answer\n",
        "  When we say missing values we mean that there are some empty spots in the table where information is supposed to be, but it's not there."
      ],
      "metadata": {
        "id": "FoU2hrnBnvGw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "titanic = sns.load_dataset('titanic')\n",
        "missing_values = titanic.isnull().sum()\n",
        "print(missing_values)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k0Izdbv6oGMc",
        "outputId": "8afca547-0874-4a16-92ed-8a8d193a3e49"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "survived         0\n",
            "pclass           0\n",
            "sex              0\n",
            "age            177\n",
            "sibsp            0\n",
            "parch            0\n",
            "fare             0\n",
            "embarked         2\n",
            "class            0\n",
            "who              0\n",
            "adult_male       0\n",
            "deck           688\n",
            "embark_town      2\n",
            "alive            0\n",
            "alone            0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9.  Use df[\"Age\"].hist() to visualize the age distribution.\n",
        "What shape do you see\n",
        "\n",
        "What might be the reason for the skew?\n"
      ],
      "metadata": {
        "id": "mp7hjQj2p6HR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "titanic = sns.load_dataset('titanic')\n",
        "titanic[\"age\"].hist(bins=20, edgecolor='black')\n",
        "plt.title('Age Distribution of Titanic Passengers')\n",
        "plt.xlabel('Age')\n",
        "plt.ylabel('Frequency')\n",
        "plt.show()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "sDhE4t56p-8Z",
        "outputId": "8153f5e0-c799-4b02-f441-2462c20b7201"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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3PsDLNtj6SczD2OzYScoKAi+vr7Yt2+fMdzk5eXh2LFjGD9+PAAgLCwMOTk5OHnyJNq0aQMA2L9/PwwGA0JDQ+9bW61WQ61Wl1muUqkk3RFS17M1cu8PYI9yIPf+APYoB3LvD7BMjxWtZ9Wwk5+fj4sXLxofp6Sk4PTp0/Dw8EBgYCAmT56M+fPno0GDBggKCsLMmTPh7++P/v37AwAaN26MZ599FmPHjkVsbCx0Oh0mTpyIIUOG8EwsIiIiAmDlsHPixAl069bN+Lj0o6XIyEisW7cO77zzDgoKCjBu3Djk5OSgY8eO2LVrFxwdHY3fs2HDBkycOBHdu3eHUqnEwIEDsWzZskfeCxEREdkmq4adrl27Qghx3/UKhQLz5s3DvHnz7ruNh4cHNm7caInhERERkQzY7JwdIluRmpqKzMxMyet6eXkhMDBQ8rpERGSKYYfoAa5evYomTZuhuKhipzdWhqPGCUl/nmfgISKyMIYdogfIyspCcVEhPPtMg8ozQLK6uqwryNoZjczMTIYdIiILY9ghqgCVZwDUvvWtPQwiIjKDzd4bi4iIiEgKDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGsMO0RERCRrDDtEREQkaww7REREJGv21h4A0ePs/PnzFqnr5eWFwMBAi9QmIqpuGHaIrECffwtQKDB8+HCL1HfUOCHpz/MMPEREYNghsgqDNh8QAp59pkHlGSBpbV3WFWTtjEZmZibDDhERGHaIrErlGQC1b31rD4OISNYYdohk6mHzgQwGAwAgMTERSmXFz1XgfCAiqm4YdohkpqLzgTQaDTZt2oTOnTujqKiowvU5H4iIqhuGHSKZqeh8IEd7BQDAZ+giFJeICtXmfCAiqo4Ydohk6mHzgRzsBAA9HHzqQegVj25gRESPGC8qSERERLLGsENERESyxrBDREREssawQ0RERLLGsENERESyxrBDREREssawQ0RERLJm02FHr9dj5syZCAoKgkajQXBwMD788EMI8b8LoAkhMGvWLPj5+UGj0SA8PBzJyclWHDURERHZEpsOO4sXL8bq1auxYsUKnD9/HosXL8aSJUuwfPly4zZLlizBsmXLEBsbi2PHjsHZ2RkREREoLi624siJiIjIVtj0FZSPHDmCfv36oXfv3gCAunXrYtOmTfjtt98A3D2qExMTgw8++AD9+vUDAKxfvx4+Pj7Yvn07hgwZYrWxExERkW2w6bDz9NNP47PPPsOFCxfQsGFDJCYm4vDhw1i6dCkAICUlBWlpaQgPDzd+j5ubG0JDQ3H06NH7hh2tVgutVmt8nJeXBwDQ6XTQ6XRVHndpDSlq2SK59wf8rzeDwQCNRgNHe8X/v72CNEpUdhapW5naaqUw+W9FKOwV0Gg0MBgMNr//H6f3KXusvuTeH2DZHitaUyH+OQHGxhgMBrz33ntYsmQJ7OzsoNfrsWDBAsyYMQPA3SM/HTp0wPXr1+Hn52f8vkGDBkGhUODrr78ut+6cOXMwd+7cMss3btwIJycnyzRDREREkiosLMTQoUORm5sLV1fX+25n00d2Nm/ejA0bNmDjxo1o2rQpTp8+jcmTJ8Pf3x+RkZFm150xYwamTp1qfJyXl4eAgAD07NnzgS9WRel0OiQkJKBHjx5QqVRVrmdr5N4f8L8e/fz80LVrV/gMXQQHn3qS1S84/zOydy2XvG5laquVAh+2NWDmCSW0hordCPRO+iWkb5yOQ4cOoWXLllIN2SIep/cpe6y+5N4fYNkeSz+ZeRibDjtvv/02pk+fbvw4qnnz5rh8+TIWLlyIyMhI+Pr6AgDS09NNjuykp6ejVatW962rVquhVqvLLFepVJLuCKnr2Rq59wcASqUSRUVFKC4Rkt4ZvFint0hdc2prDQpoKzgGbYlAUVERlEpltdn3j8P7lD1Wf3LvD7BMjxWtZ9Nhp7CwEEql6QljdnZ2MBgMAICgoCD4+vpi3759xnCTl5eHY8eOYfz48Y96uGRFqampyMzMlKxe6XssKSlJsppERGQdNh12+vbtiwULFiAwMBBNmzbFqVOnsHTpUowePRoAoFAoMHnyZMyfPx8NGjRAUFAQZs6cCX9/f/Tv39+6g6dHJjU1FY1CGqO4qFCymhqNBps2bcLYsWMlq0lERNZh02Fn+fLlmDlzJt544w1kZGTA398fr732GmbNmmXc5p133kFBQQHGjRuHnJwcdOzYEbt27YKjo6MVR06PUmZmJoqLCuHZZxpUngGS1HS0v/uxjuvTg1G0b50kNYmIyDpsOuy4uLggJiYGMTEx991GoVBg3rx5mDdv3qMbGNkklWcA1L71Jal195RtPexdvSWpR0RE1mPTV1AmIiIiqiqGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNYYdIiIikjWGHSIiIpI1hh0iIiKSNXtrD4CIqp/z589LXtPLywuBgYGS1yUiYtghogrT598CFAoMHz5c8tqOGick/XmegYeIJMewQ0QVZtDmA0LAs880qDwDJKury7qCrJ3RyMzMZNghIskx7BBRpak8A6D2rW/tYRARVQgnKBMREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkawx7BAREZGsMewQERGRrDHsEBERkazZfNi5du0ahg8fDk9PT2g0GjRv3hwnTpwwrhdCYNasWfDz84NGo0F4eDiSk5OtOGIiIiKyJTYddm7duoUOHTpApVLhxx9/xB9//IHo6GjUrFnTuM2SJUuwbNkyxMbG4tixY3B2dkZERASKi4utOHIiIiKyFfbmfNOlS5dQr149qcdSxuLFixEQEIC4uDjjsqCgIOP/CyEQExODDz74AP369QMArF+/Hj4+Pti+fTuGDBli8TESERGRbTMr7NSv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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The histogram of ages is right-skewed which is right skewed means that the data has a long tail on the right this means there are more younger passengers and fewer older passengers\n"
      ],
      "metadata": {
        "id": "k7Qb3kSFUXVp"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "10. What does it mean if a column has a high standard deviation?\n",
        "\n",
        "  Create a list or column that has a low and a high std. dev, and compare.  \n",
        "answer\n",
        "A high standard deviation means the numbers in the column are very different from each other with some numbers being higher or lower than the average or the numbers are not close to each other.\n"
      ],
      "metadata": {
        "id": "dsjGI3NIsON7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "A = [60, 65, 70, 75, 80]\n",
        "B = [40, 50, 90, 60, 100]\n",
        "def calstdev(scores):\n",
        "    mean = sum(scores) / len(scores)\n",
        "    variance = sum((x - mean) ** 2 for x in scores) / len(scores)\n",
        "    return math.sqrt(variance)\n",
        "STDVA = calstdev(A)\n",
        "STDVB= calstdev(B)\n",
        "print(f\"Course A standard deviation: {STDVA}\")\n",
        "print(f\"Course B standard deviation: {STDVB}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sm0hyLAStgxi",
        "outputId": "2353779c-6343-48a7-b945-be40d110bed0"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Course A standard deviation: 7.0710678118654755\n",
            "Course B standard deviation: 23.15167380558045\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "11.What are some real-world problems where missing data might affect results? Give 2 examples.\n",
        "answer\n",
        "1,Student Grades If some students exam scores or assignment marks are missing, it can make their final grades wrong. For example, if a student score on an important test is missing, their overall grade may not show how well they really did. This could affect if they pass or fail.\n",
        "2,If some voting data is missing or not recorded correctly, the government may not know the true results of an election. For example, if votes from certain areas are not counted, it could make it look like fewer people voted, and the government might make wrong decisions about who should represent the people."
      ],
      "metadata": {
        "id": "aaYGxvuEvrZL"
      }
    }
  ]
}
