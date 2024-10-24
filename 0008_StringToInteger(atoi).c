int	ft_space(char c)
{
	if (c == ' ' || c == '\n' || c == '\t' || c == '\v' || c == '\f' || c == '\r')
		return (1);
	else
		return (0);
}

int	ft_getnum(char *str, int *sign)
{
	int	i;

	*sign = 1;
	i = 0;
	while (ft_space(str[i]))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			*sign *= -1;
		i++;
        if (str[i] == '+' || str[i] == '-')
            return (0);
	}
	return (i);
}

int myAtoi(char* s) {
    int	result;
	int	sign;
	int	i;

    int MAX_INT = 2147483647;
	int MIN_INT = -2147483648;

	result = 0;
	i = ft_getnum(s, &sign);
	while (s[i] >= '0' && s[i] <= '9')
	{
        if (result > (MAX_INT - (s[i] - '0')) / 10)
        {
            if (sign == 1)
                return MAX_INT;
            else
                return MIN_INT;
        }
		result *= 10;
		result += (s[i] - '0');
	    i++;
    }
	return (result * sign);
}